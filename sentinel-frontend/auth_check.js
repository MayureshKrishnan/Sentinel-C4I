// Sentinel V2 C4I Unified Session Core & Access Guard
(function() {
  const token = localStorage.getItem('auth_token') || sessionStorage.getItem('auth_token');
  const path = window.location.pathname.toLowerCase();
  
  // Restricted tactical command consoles that require authenticated clearance
  const isProtectedPage = path.endsWith('dashboard.html') || 
                          path.endsWith('officer_console.html') || 
                          path.endsWith('pipeline.html') ||
                          path.endsWith('/dashboard') ||
                          path.endsWith('/officer_console') ||
                          path.endsWith('/pipeline');

  if (isProtectedPage && !token) {
    // Preserve requested target URL for seamless return after authentication
    try {
      sessionStorage.setItem('redirect_after_login', window.location.href);
    } catch (e) {}
    window.location.replace('login.html?restricted=1');
  }
})();

function sentinelLogout() {
  localStorage.removeItem('auth_token');
  localStorage.removeItem('sentinel_role');
  localStorage.removeItem('sentinel_op_id');
  localStorage.removeItem('sentinel_status');
  sessionStorage.removeItem('auth_token');
  sessionStorage.removeItem('redirect_after_login');
  window.location.replace('login.html?logged_out=1');
}
