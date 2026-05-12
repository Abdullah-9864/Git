// ═══════════════════════════════════════════════════════════
//  src/pages/UsersPage.jsx  —  HOOKS, STATE, FETCH, CRUD
//
//  This page teaches the most important React concepts:
//
//  useState(initialValue)
//    Stores data that can change. When it changes, React
//    re-renders the component automatically.
//    Returns [currentValue, setterFunction].
//
//  useEffect(fn, [deps])
//    Runs AFTER the component renders.
//    deps = dependency array:
//      []    → runs once when component first mounts
//      [x]   → runs again whenever x changes
//      none  → runs after every render (usually a bug)
//
//  fetch()
//    Browser built-in to make HTTP requests.
//    Returns a Promise — async/await is the cleanest way to use it.
// ═══════════════════════════════════════════════════════════

import { useState, useEffect } from 'react';

const API = 'http://localhost:3001/api/users';

function UsersPage() {
  // ── STATE ──────────────────────────────────────────────
  const [users,   setUsers]   = useState([]);      // the list of users from the API
  const [loading, setLoading] = useState(true);    // are we waiting for data?
  const [error,   setError]   = useState(null);    // any error message
  const [form,    setForm]    = useState({ name: '', role: '' }); // the "add user" form
  const [msg,     setMsg]     = useState('');      // success/error flash message

  // ── FETCH ALL USERS (on mount) ─────────────────────────
  useEffect(() => {
    fetchUsers();
  }, []); // empty array = run once when component mounts

  async function fetchUsers() {
    try {
      setLoading(true);
      const res  = await fetch(API);    // GET /api/users
      const data = await res.json();    // parse the JSON body
      setUsers(data);                   // store in state → triggers re-render
    } catch (err) {
      setError('Could not connect to the server. Is it running?');
    } finally {
      setLoading(false);
    }
  }

  // ── CREATE USER ────────────────────────────────────────
  async function handleCreate(e) {
    e.preventDefault(); // prevent the browser's default form submit (page reload)

    const res = await fetch(API, {
      method:  'POST',
      headers: { 'Content-Type': 'application/json' }, // tell server what format we're sending
      body:    JSON.stringify(form),                    // convert JS object to JSON string
    });

    if (res.ok) {
      const newUser = await res.json();
      setUsers([...users, newUser]); // spread existing + add new (don't mutate state directly)
      setForm({ name: '', role: '' }); // reset form
      flash('User created!');
    } else {
      const err = await res.json();
      flash(err.error, true);
    }
  }

  // ── DELETE USER ────────────────────────────────────────
  async function handleDelete(id) {
    const res = await fetch(`${API}/${id}`, { method: 'DELETE' });

    if (res.ok) {
      setUsers(users.filter(u => u.id !== id)); // remove from state without re-fetching
      flash('User deleted.');
    }
  }

  function flash(text, isError = false) {
    setMsg(isError ? `Error: ${text}` : text);
    setTimeout(() => setMsg(''), 3000); // clear after 3 seconds
  }

  // ── RENDER ──────────────────────────────────────────────
  // Conditional rendering — show different UI based on state.
  if (loading) return <p style={styles.muted}>Loading users from API…</p>;
  if (error)   return <p style={{ color: 'red' }}>{error}</p>;

  return (
    <div>
      <h1 style={styles.h1}>Users</h1>
      <p style={styles.sub}>Full CRUD — talks to <code>GET/POST/DELETE /api/users</code></p>

      {msg && <div style={styles.flash}>{msg}</div>}

      {/* CREATE FORM */}
      <form onSubmit={handleCreate} style={styles.form}>
        <input
          style={styles.input}
          placeholder="Name"
          value={form.name}
          onChange={e => setForm({ ...form, name: e.target.value })}
          // onChange fires on every keystroke.
          // e.target.value = what's in the input box.
          // We spread the old form and overwrite just "name" — controlled input pattern.
        />
        <input
          style={styles.input}
          placeholder="Role"
          value={form.role}
          onChange={e => setForm({ ...form, role: e.target.value })}
        />
        <button type="submit" style={styles.btn}>Add user</button>
      </form>

      {/* USER LIST */}
      {users.length === 0 ? (
        <p style={styles.muted}>No users yet.</p>
      ) : (
        <ul style={styles.list}>
          {users.map(user => (
            // key= is required when rendering lists.
            // React uses it to track which item is which when the list changes.
            // Always use a unique, stable ID — never use array index.
            <li key={user.id} style={styles.item}>
              <span>
                <strong>{user.name}</strong>
                <span style={styles.muted}> — {user.role}</span>
                <span style={styles.id}> #{user.id}</span>
              </span>
              <button
                onClick={() => handleDelete(user.id)}
                style={styles.delBtn}
              >
                delete
              </button>
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}

const styles = {
  h1:    { fontSize: '1.8rem', fontWeight: 'bold', marginBottom: '0.25rem' },
  sub:   { color: '#666', fontSize: '0.88rem', marginBottom: '1.5rem' },
  flash: { background: '#e8f5e9', border: '1px solid #a5d6a7', padding: '0.5rem 0.75rem', borderRadius: '4px', marginBottom: '1rem', fontSize: '0.9rem' },
  form:  { display: 'flex', gap: '0.5rem', marginBottom: '1.5rem', flexWrap: 'wrap' },
  input: { padding: '0.4rem 0.75rem', border: '1px solid #ddd', borderRadius: '4px', fontSize: '0.9rem', flex: 1, minWidth: '140px' },
  btn:   { padding: '0.4rem 1rem', background: '#1a1a1a', color: '#fff', border: 'none', borderRadius: '4px', cursor: 'pointer', fontSize: '0.9rem' },
  list:  { listStyle: 'none', display: 'flex', flexDirection: 'column', gap: '0.5rem' },
  item:  { display: 'flex', justifyContent: 'space-between', alignItems: 'center', padding: '0.75rem 1rem', border: '1px solid #eee', borderRadius: '6px', background: '#fff' },
  muted: { color: '#888', fontSize: '0.88rem' },
  id:    { color: '#bbb', fontSize: '0.8rem' },
  delBtn:{ background: 'none', border: '1px solid #ddd', borderRadius: '4px', padding: '2px 8px', cursor: 'pointer', fontSize: '0.8rem', color: '#888' },
};

export default UsersPage;
