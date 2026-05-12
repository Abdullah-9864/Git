// ═══════════════════════════════════════════════════════════
//  src/components/Navbar.jsx  —  A REUSABLE COMPONENT
//
//  Components are the building blocks of React UIs.
//  This Navbar is defined once and used in App.jsx.
//  It renders on every page automatically.
//
//  <Link> from react-router-dom:
//  Renders as an <a> tag but intercepts the click.
//  Instead of loading a new page (full browser request),
//  it tells React Router to swap the component — instant.
// ═══════════════════════════════════════════════════════════

import { Link, useLocation } from 'react-router-dom';
// useLocation is a HOOK — it gives you the current URL object.
// We use it to highlight the active nav link.

const links = [
  { to: '/',         label: 'Home'     },
  { to: '/users',    label: 'Users'    },
  { to: '/posts',    label: 'Posts'    },
  { to: '/concepts', label: 'Concepts' },
];

function Navbar() {
  const location = useLocation(); // { pathname: '/users', search: '', ... }

  return (
    <nav style={styles.nav}>
      <span style={styles.brand}>webdev-learn</span>
      <div style={styles.links}>
        {links.map(link => {
          const isActive = location.pathname === link.to;
          return (
            <Link
              key={link.to}
              to={link.to}
              style={{ ...styles.link, ...(isActive ? styles.active : {}) }}
            >
              {link.label}
            </Link>
          );
        })}
      </div>
    </nav>
  );
}

const styles = {
  nav:    { display: 'flex', alignItems: 'center', gap: '2rem', padding: '1rem 1.5rem', borderBottom: '1px solid #ddd', background: '#fff' },
  brand:  { fontWeight: 'bold', letterSpacing: '-0.5px' },
  links:  { display: 'flex', gap: '1.5rem' },
  link:   { fontSize: '0.9rem', color: '#666', padding: '2px 0', borderBottom: '2px solid transparent' },
  active: { color: '#1a1a1a', borderBottom: '2px solid #1a1a1a' },
};

export default Navbar;
