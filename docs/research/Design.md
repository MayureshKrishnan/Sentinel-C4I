# SENTINEL - Design System & UI/UX Guidelines (Design.md)

## 1. Design Aesthetics & Visual Identity
SENTINEL utilizes a **Tactical Command Center / Dark Glassmorphism** visual theme. The interface gives coordinators immediate visual clarity under high stress, avoiding generic browser defaults and emphasizing high-contrast readability.

---

## 2. Color Palette & Priority Tokens

### Base Theme Palette
* **Deep Space Background**: `#060B19`
* **Card & Panel Surface**: `#0F172A` (with subtle backdrop blur `backdrop-filter: blur(12px)`)
* **Panel Border / Glass Stroke**: `rgba(255, 255, 255, 0.08)`
* **Primary Text**: `#F8FAFC`
* **Secondary / Muted Text**: `#94A3B8`
* **Accent Cyan**: `#38BDF8` / `#00F5D4`

### Priority Indicator Colors

| Priority Level | Score Range | Primary Color | Hex Code | Visual Badge Style | Map Marker |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **CRITICAL** | 70 – 100 | Vivid Crimson | `#EF4444` | Red Glow + Pulsing Border | Red Marker |
| **MEDIUM** | 35 – 69 | Amber Gold | `#F59E0B` | Amber Solid Badge | Amber Marker |
| **LOW** | 0 – 34 | Slate Muted | `#64748B` | Subtle Grey Badge | Grey Marker |
| **VOLUNTEER** | Live Tracker | Neon Teal | `#10B981` | Glowing Cyan Pill | Cyan Pin |

---

## 3. Typography System
* **Primary Font Family**: `'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif`
* **Monospace Font** (Coordinates, Timestamps, Scores): `'JetBrains Mono', 'Fira Code', monospace`

### Scale & Hierarchy
* **Dashboard Header Title**: `20px / 1.2`, Semi-Bold (`font-semibold`), Letter Spacing `0.05em`
* **Section / Panel Title**: `14px / 1.4`, Medium (`font-medium`), Uppercase (`tracking-wider`), Color `#94A3B8`
* **Score Pill Badge**: `16px`, Extra-Bold (`font-extrabold`), Monospace
* **Body / Tip Text**: `13px / 1.5`, Regular (`font-normal`), Color `#E2E8F0`

---

## 4. UI Component Patterns

### Glassmorphism Panel
```css
.glass-panel {
  background: rgba(15, 23, 42, 0.75);
  backdrop-filter: blur(12px);
  -webkit-backdrop-filter: blur(12px);
  border: 1px solid rgba(255, 255, 255, 0.08);
  border-radius: 12px;
  box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
}
```

### Micro-Animations
* **Map Pin Drop**: Smooth bounce transition when a new tip arrives via WebSockets.
* **Critical Pulse**: Infinite keyframe opacity pulse (`0.8` to `1.0`) on Critical score cards.
* **Timeline Slider**: Smooth drag transitions updating heatmap layers without frame drops.
