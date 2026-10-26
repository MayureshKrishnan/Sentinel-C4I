-- Sentinel V2 Database Schema (PostgreSQL) - Schema v3

-- APP ROLE (Non-owner, NOLOGIN, no bypass RLS)
DO $$ BEGIN
    CREATE ROLE sentinel_app WITH NOLOGIN NOSUPERUSER NOBYPASSRLS;
EXCEPTION
    WHEN duplicate_object THEN null;
END $$;

-- LOGIN ROLE
DO $$ BEGIN
    CREATE ROLE sentinel_login WITH LOGIN PASSWORD 'CHANGE_ME' NOSUPERUSER NOBYPASSRLS;
EXCEPTION
    WHEN duplicate_object THEN null;
END $$;

-- Grant app role to login role
GRANT sentinel_app TO sentinel_login;

-- ISOLATED SCHEMA
CREATE SCHEMA IF NOT EXISTS sentinel;
GRANT USAGE ON SCHEMA sentinel TO sentinel_app;

-- -----------------------------------------------------------------------------
-- TABLES (Created inside 'sentinel' schema)
-- -----------------------------------------------------------------------------

CREATE TABLE sentinel.jurisdictions (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    name VARCHAR(255) NOT NULL,
    level VARCHAR(50) NOT NULL CHECK (level IN ('state', 'district', 'station')),
    parent_id UUID REFERENCES sentinel.jurisdictions(id) ON DELETE RESTRICT,
    created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE sentinel.users (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    email VARCHAR(255) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    role VARCHAR(50) NOT NULL CHECK (role IN ('reviewer', 'case_officer', 'supervisor', 'admin', 'auditor')),
    status VARCHAR(50) NOT NULL DEFAULT 'active' CHECK (status IN ('active', 'suspended')),
    mfa_secret VARCHAR(255), 
    mfa_enabled BOOLEAN NOT NULL DEFAULT FALSE,
    failed_logins INT NOT NULL DEFAULT 0,
    locked_until TIMESTAMPTZ,
    created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE sentinel.user_jurisdictions (
    user_id UUID REFERENCES sentinel.users(id) ON DELETE CASCADE,
    jurisdiction_id UUID REFERENCES sentinel.jurisdictions(id) ON DELETE CASCADE,
    PRIMARY KEY (user_id, jurisdiction_id)
);

CREATE TABLE sentinel.refresh_tokens (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID REFERENCES sentinel.users(id) ON DELETE CASCADE,
    family_id UUID NOT NULL,
    token_hash VARCHAR(255) UNIQUE NOT NULL,
    expires_at TIMESTAMPTZ NOT NULL,
    revoked_at TIMESTAMPTZ,
    replaced_by UUID,
    created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE sentinel.tips (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    status VARCHAR(50) NOT NULL DEFAULT 'PENDING' CHECK (status IN ('PENDING', 'CONFIRMED', 'REJECTED', 'EXPIRED', 'ESCALATED')),
    version INT NOT NULL DEFAULT 1,
    signal_type VARCHAR(50) NOT NULL,
    is_simulated BOOLEAN NOT NULL DEFAULT FALSE,
    jurisdiction_id UUID REFERENCES sentinel.jurisdictions(id) ON DELETE RESTRICT,
    lat DOUBLE PRECISION CHECK (lat >= -90 AND lat <= 90),
    lng DOUBLE PRECISION CHECK (lng >= -180 AND lng <= 180),
    source VARCHAR(255),
    score INT CHECK (score >= 0 AND score <= 100),
    message TEXT,
    created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE sentinel.tip_decisions (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tip_id UUID REFERENCES sentinel.tips(id) ON DELETE RESTRICT,
    user_id UUID REFERENCES sentinel.users(id) ON DELETE RESTRICT,
    decision VARCHAR(50) NOT NULL CHECK (decision IN ('CONFIRMED', 'REJECTED', 'ESCALATED')),
    reason_code VARCHAR(100) NOT NULL,
    note TEXT,
    created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE sentinel.idempotency_keys (
    key VARCHAR(255) PRIMARY KEY,
    created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP
);

-- AUDIT LOG (Append Only, Serialized Hash Chain)
CREATE TABLE sentinel.audit_log (
    seq_id BIGSERIAL PRIMARY KEY,
    id UUID UNIQUE DEFAULT gen_random_uuid(),
    entry_hash VARCHAR(64) NOT NULL,
    prev_hash VARCHAR(64) NOT NULL,
    user_id UUID,
    action VARCHAR(255) NOT NULL,
    details JSONB NOT NULL,
    model_version VARCHAR(50),
    created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP
);

-- -----------------------------------------------------------------------------
-- ROW LEVEL SECURITY (RLS)
-- -----------------------------------------------------------------------------
ALTER TABLE sentinel.jurisdictions ENABLE ROW LEVEL SECURITY;
ALTER TABLE sentinel.users ENABLE ROW LEVEL SECURITY;
ALTER TABLE sentinel.user_jurisdictions ENABLE ROW LEVEL SECURITY;
ALTER TABLE sentinel.refresh_tokens ENABLE ROW LEVEL SECURITY;
ALTER TABLE sentinel.tips ENABLE ROW LEVEL SECURITY;
ALTER TABLE sentinel.tip_decisions ENABLE ROW LEVEL SECURITY;
ALTER TABLE sentinel.idempotency_keys ENABLE ROW LEVEL SECURITY;
ALTER TABLE sentinel.audit_log ENABLE ROW LEVEL SECURITY;

ALTER TABLE sentinel.jurisdictions FORCE ROW LEVEL SECURITY;
ALTER TABLE sentinel.users FORCE ROW LEVEL SECURITY;
ALTER TABLE sentinel.user_jurisdictions FORCE ROW LEVEL SECURITY;
ALTER TABLE sentinel.refresh_tokens FORCE ROW LEVEL SECURITY;
ALTER TABLE sentinel.tips FORCE ROW LEVEL SECURITY;
ALTER TABLE sentinel.tip_decisions FORCE ROW LEVEL SECURITY;
ALTER TABLE sentinel.idempotency_keys FORCE ROW LEVEL SECURITY;
ALTER TABLE sentinel.audit_log FORCE ROW LEVEL SECURITY;

-- Explicit RLS Policies driven by transaction settings
CREATE POLICY select_jurisdictions ON sentinel.jurisdictions 
    FOR SELECT TO sentinel_app 
    USING (true); -- Usually public info within app context

CREATE POLICY select_users ON sentinel.users 
    FOR SELECT TO sentinel_app 
    USING (true);

CREATE POLICY own_jurisdictions ON sentinel.user_jurisdictions
    FOR SELECT TO sentinel_app
    USING (user_id = nullif(current_setting('app.user_id', true), '')::uuid);

CREATE POLICY select_tokens ON sentinel.refresh_tokens 
    FOR SELECT TO sentinel_app 
    USING (user_id = nullif(current_setting('app.user_id', true), '')::uuid);

CREATE POLICY insert_tokens ON sentinel.refresh_tokens 
    FOR INSERT TO sentinel_app 
    WITH CHECK (user_id = nullif(current_setting('app.user_id', true), '')::uuid);

CREATE POLICY update_tokens ON sentinel.refresh_tokens 
    FOR UPDATE TO sentinel_app 
    USING (user_id = nullif(current_setting('app.user_id', true), '')::uuid);

CREATE POLICY tip_jurisdiction ON sentinel.tips
    FOR SELECT TO sentinel_app
    USING (
        jurisdiction_id IN (
            SELECT jurisdiction_id FROM sentinel.user_jurisdictions 
            WHERE user_id = nullif(current_setting('app.user_id', true), '')::uuid
        )
    );

CREATE POLICY tip_decisions_access ON sentinel.tip_decisions 
    FOR SELECT TO sentinel_app 
    USING (
        user_id = nullif(current_setting('app.user_id', true), '')::uuid
    );

CREATE POLICY select_audit ON sentinel.audit_log FOR SELECT TO sentinel_app USING (true);
CREATE POLICY all_idempotency ON sentinel.idempotency_keys TO sentinel_app USING (true) WITH CHECK (true);

-- Grants
GRANT SELECT ON sentinel.jurisdictions TO sentinel_app;
GRANT SELECT, INSERT ON sentinel.users TO sentinel_app;
GRANT UPDATE (failed_logins, locked_until, mfa_enabled, mfa_secret, updated_at) ON sentinel.users TO sentinel_app;
GRANT SELECT ON sentinel.user_jurisdictions TO sentinel_app;
GRANT SELECT, INSERT, UPDATE ON sentinel.refresh_tokens TO sentinel_app;
GRANT SELECT, INSERT, UPDATE ON sentinel.tips TO sentinel_app;
GRANT SELECT, INSERT ON sentinel.tip_decisions TO sentinel_app;
GRANT SELECT, INSERT ON sentinel.idempotency_keys TO sentinel_app;
GRANT SELECT ON sentinel.audit_log TO sentinel_app; 

-- -----------------------------------------------------------------------------
-- AUDIT LOG PROTECTIONS
-- -----------------------------------------------------------------------------
CREATE OR REPLACE FUNCTION sentinel.block_audit_modification()
RETURNS TRIGGER AS $$
BEGIN
    RAISE EXCEPTION 'Audit log is append-only. Modification/Truncation is forbidden.';
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trg_block_audit_update
BEFORE UPDATE OR DELETE OR TRUNCATE ON sentinel.audit_log
FOR EACH STATEMENT EXECUTE FUNCTION sentinel.block_audit_modification();

REVOKE TRUNCATE ON sentinel.audit_log FROM sentinel_app;

-- ADVISORY LOCK FUNCTION FOR AUDIT LOG SERIALIZATION
CREATE OR REPLACE FUNCTION sentinel.insert_audit_entry(
    p_action VARCHAR,
    p_details JSONB,
    p_model_version VARCHAR
) RETURNS UUID AS $$
DECLARE
    v_prev_hash VARCHAR(64);
    v_entry_hash VARCHAR(64);
    v_id UUID;
    v_seq_id BIGINT;
    v_lock_key CONSTANT BIGINT := 123456789;
    v_uid UUID;
    v_ts TIMESTAMPTZ;
BEGIN
    PERFORM pg_advisory_xact_lock(v_lock_key);
    
    v_uid := nullif(current_setting('app.user_id', true), '')::uuid;
    v_id := gen_random_uuid();
    v_ts := CURRENT_TIMESTAMP;

    SELECT entry_hash INTO v_prev_hash FROM sentinel.audit_log ORDER BY seq_id DESC LIMIT 1;
    IF v_prev_hash IS NULL THEN
        v_prev_hash := 'genesis';
    END IF;
    
    -- Insert first to get seq_id
    INSERT INTO sentinel.audit_log (id, user_id, action, details, model_version, prev_hash, entry_hash, created_at)
    VALUES (v_id, v_uid, p_action, COALESCE(p_details, '{}'::jsonb), p_model_version, v_prev_hash, 'temp_hash', v_ts)
    RETURNING seq_id INTO v_seq_id;
    
    -- Calculate new hash covering all fields, delimited
    v_entry_hash := encode(sha256(convert_to(concat_ws('|', 
        v_prev_hash, 
        v_seq_id::text, 
        v_id::text,
        COALESCE(v_uid::text, ''), 
        p_action, 
        COALESCE(p_model_version, ''), 
        (SELECT COALESCE(jsonb_object_agg(key, value ORDER BY key), '{}'::jsonb) FROM jsonb_each(COALESCE(p_details, '{}'::jsonb)))::text,
        v_ts::text
    ), 'UTF8')), 'hex');
    
    -- Update with actual hash
    UPDATE sentinel.audit_log SET entry_hash = v_entry_hash WHERE seq_id = v_seq_id;
    
    RETURN v_id;
END;
$$ LANGUAGE plpgsql SECURITY DEFINER SET search_path = sentinel, pg_temp;

REVOKE ALL ON FUNCTION sentinel.insert_audit_entry(varchar, jsonb, varchar) FROM PUBLIC;
GRANT EXECUTE ON FUNCTION sentinel.insert_audit_entry TO sentinel_app;
