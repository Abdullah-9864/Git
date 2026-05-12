// ═══════════════════════════════════════════════════════════
//  src/pages/ConceptsPage.jsx  —  GLOSSARY / REFERENCE
//
//  A plain reference page. No API calls here.
//  Shows how to render a list of static data as UI.
// ═══════════════════════════════════════════════════════════

const concepts = [
  {
    term: 'Server',
    plain: 'A program that runs 24/7 waiting for requests. When one arrives, it processes it and sends a response back.',
    code: 'app.listen(3001)',
  },
  {
    term: 'HTTP',
    plain: 'The language browsers and servers use to communicate. Every interaction is a Request → Response pair.',
    code: 'GET /api/users  →  200 OK + JSON',
  },
  {
    term: 'REST API',
    plain: 'A naming convention for server URLs. Each URL represents a "resource" (users, posts). The HTTP method tells the server what to do with it.',
    code: 'GET /posts    → list\nPOST /posts   → create\nDELETE /posts/1 → delete',
  },
  {
    term: 'Middleware',
    plain: 'A function that runs on every request before it reaches your route. Useful for logging, authentication, parsing JSON.',
    code: 'app.use((req, res, next) => {\n  console.log(req.method, req.url);\n  next(); // must call this!\n});',
  },
  {
    term: 'Route params',
    plain: 'Named wildcards in a URL. /users/:id matches /users/1, /users/42, etc. The value is in req.params.id.',
    code: "app.get('/users/:id', (req, res) => {\n  const id = req.params.id; // '1'\n});",
  },
  {
    term: 'Query params',
    plain: 'Key=value pairs after ? in a URL. Used for filtering, searching, pagination — not for identifying a specific resource.',
    code: "GET /posts?search=hello\n// req.query = { search: 'hello' }",
  },
  {
    term: 'req.body',
    plain: 'The data the client sent in the request body. Only available in POST/PUT. Requires express.json() middleware to parse.',
    code: "app.post('/users', (req, res) => {\n  const { name } = req.body;\n});",
  },
  {
    term: 'Status codes',
    plain: '200 = OK. 201 = Created. 400 = Bad request (your fault). 404 = Not found. 500 = Server error (my fault).',
    code: "res.status(404).json({ error: 'Not found' })",
  },
  {
    term: 'CORS',
    plain: 'Browsers block requests from one origin (localhost:5173) to another (localhost:3001) by default. The cors() middleware unlocks it.',
    code: "app.use(cors()) // in Express\n// Now React can call your API",
  },
  {
    term: 'useState',
    plain: 'React hook to store data that can change. When you call the setter, React re-renders the component with the new value.',
    code: "const [count, setCount] = useState(0);\nsetCount(count + 1); // triggers re-render",
  },
  {
    term: 'useEffect',
    plain: 'React hook that runs code after rendering. The dependency array controls when it re-runs. Empty [] = runs once on mount.',
    code: "useEffect(() => {\n  fetchData(); // runs once\n}, []); // empty = on mount only",
  },
  {
    term: 'fetch()',
    plain: 'Browser built-in for HTTP requests. Returns a Promise. Use async/await to keep the code readable.',
    code: "const res  = await fetch('/api/users');\nconst data = await res.json();",
  },
  {
    term: 'Props',
    plain: 'Data passed from a parent component to a child. Like function arguments. The child receives them as a plain object.',
    code: "<Card title='Hello' />\n// inside Card:\nfunction Card({ title }) { ... }",
  },
  {
    term: 'JSX',
    plain: 'HTML-like syntax in JavaScript. It compiles to React.createElement() calls. Use className instead of class.',
    code: "// JSX\n<div className='box'>Hello</div>\n// compiles to:\nReact.createElement('div', {className:'box'}, 'Hello')",
  },
  {
    term: 'Client-side routing',
    plain: 'React Router intercepts link clicks and swaps components without the browser fetching a new page. Feels instant.',
    code: "<Link to='/users'>Users</Link>\n// no page reload — component swaps",
  },
];

function ConceptsPage() {
  return (
    <div>
      <h1 style={styles.h1}>Concepts</h1>
      <p style={styles.sub}>{concepts.length} things explained in plain English, with code.</p>

      <div style={styles.list}>
        {concepts.map(c => (
          <div key={c.term} style={styles.card}>
            <div style={styles.term}>{c.term}</div>
            <p style={styles.plain}>{c.plain}</p>
            <pre style={styles.code}>{c.code}</pre>
          </div>
        ))}
      </div>
    </div>
  );
}

const styles = {
  h1:    { fontSize: '1.8rem', fontWeight: 'bold', marginBottom: '0.25rem' },
  sub:   { color: '#666', fontSize: '0.88rem', marginBottom: '2rem' },
  list:  { display: 'flex', flexDirection: 'column', gap: '1rem' },
  card:  { border: '1px solid #ddd', borderRadius: '6px', padding: '1.25rem', background: '#fff' },
  term:  { fontWeight: 'bold', fontSize: '1rem', marginBottom: '0.35rem' },
  plain: { fontSize: '0.9rem', color: '#444', lineHeight: 1.6, marginBottom: '0.75rem' },
  code:  { background: '#f4f4f4', padding: '0.65rem 0.85rem', borderRadius: '4px', fontSize: '0.82rem', overflowX: 'auto', lineHeight: 1.6, margin: 0 },
};

export default ConceptsPage;
