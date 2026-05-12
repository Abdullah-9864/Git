// ═══════════════════════════════════════════════════════════
//  src/pages/Home.jsx  —  THE HOMEPAGE
//
//  This is just a page component — it's a regular function
//  that returns JSX. No special magic.
//
//  Pages live in /pages, reusable UI pieces in /components.
//  That's just a naming convention — React doesn't care.
// ═══════════════════════════════════════════════════════════

function Home() {
  return (
    <div>
      <h1 style={styles.h1}>Hello World.</h1>
      <p style={styles.sub}>A minimal site that explains everything about full-stack web development.</p>

      <div style={styles.grid}>
        <Card
          title="How this site works"
          body="React (frontend) talks to Express (backend) over HTTP. Express serves data from an in-memory array. Navigate to Users or Posts to see real API calls happen."
        />
        <Card
          title="File structure"
          body="backend/ has your Node.js + Express server. frontend/ has your React app. They run as two separate processes on different ports."
        />
        <Card
          title="What to explore"
          body="Users page: full CRUD (create, read, update, delete). Posts page: filtering with query params. Concepts page: all the theory in one place."
        />
      </div>
    </div>
  );
}

// A small reusable component defined in the same file.
// Fine to do this for simple, single-use components.
function Card({ title, body }) {
  // { title, body } — destructured props.
  // Props = data passed from parent to child component.
  // <Card title="hello" /> → the Card function receives { title: 'hello' }
  return (
    <div style={styles.card}>
      <h3 style={styles.cardTitle}>{title}</h3>
      <p style={styles.cardBody}>{body}</p>
    </div>
  );
}

const styles = {
  h1:        { fontSize: '2.5rem', fontWeight: 'bold', marginBottom: '0.5rem' },
  sub:       { color: '#666', marginBottom: '2.5rem', fontSize: '1rem' },
  grid:      { display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(240px, 1fr))', gap: '1rem' },
  card:      { border: '1px solid #ddd', borderRadius: '6px', padding: '1.25rem', background: '#fff' },
  cardTitle: { fontWeight: 'bold', marginBottom: '0.5rem', fontSize: '0.95rem' },
  cardBody:  { fontSize: '0.88rem', color: '#555', lineHeight: 1.6 },
};

export default Home;
