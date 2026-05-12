// ═══════════════════════════════════════════════════════════
//  src/pages/PostsPage.jsx  —  QUERY PARAMS + SEARCH
//
//  New concepts:
//
//  Query parameters in fetch:
//    fetch(`/api/posts?search=${term}`)
//    The server reads req.query.search to filter results.
//
//  useEffect with dependency:
//    useEffect(() => { fetchPosts() }, [search])
//    Re-runs fetchPosts every time "search" state changes.
//    This is how you make a live search without a button.
//
//  Derived state:
//    We don't store filtered results separately.
//    We re-fetch with a different URL query param instead.
//    The server does the filtering — that's more realistic.
// ═══════════════════════════════════════════════════════════

import { useState, useEffect } from 'react';

const API = 'http://localhost:3001/api/posts';

function PostsPage() {
  const [posts,   setPosts]   = useState([]);
  const [loading, setLoading] = useState(true);
  const [search,  setSearch]  = useState('');   // the search input value
  const [form,    setForm]    = useState({ title: '', body: '', author: '' });
  const [msg,     setMsg]     = useState('');

  // Runs whenever "search" changes (including on first mount).
  // This is a "reactive" pattern — state drives the fetch.
  useEffect(() => {
    fetchPosts();
  }, [search]); // [search] = re-run when search changes

  async function fetchPosts() {
    setLoading(true);
    try {
      // Build URL with query param if search is not empty
      const url = search ? `${API}?search=${encodeURIComponent(search)}` : API;
      // encodeURIComponent handles special characters like spaces → %20
      const res  = await fetch(url);
      const data = await res.json();
      setPosts(data);
    } catch {
      setPosts([]);
    } finally {
      setLoading(false);
    }
  }

  async function handleCreate(e) {
    e.preventDefault();
    const res = await fetch(API, {
      method:  'POST',
      headers: { 'Content-Type': 'application/json' },
      body:    JSON.stringify(form),
    });
    if (res.ok) {
      const newPost = await res.json();
      setPosts(prev => [newPost, ...prev]); // add to front of list
      // Using the "functional update" form of setState:
      // prev => [...] — React guarantees prev is the latest state.
      // Safer than using posts directly inside async functions.
      setForm({ title: '', body: '', author: '' });
      flash('Post created!');
    }
  }

  async function handleDelete(id) {
    const res = await fetch(`${API}/${id}`, { method: 'DELETE' });
    if (res.ok) {
      setPosts(prev => prev.filter(p => p.id !== id));
      flash('Post deleted.');
    }
  }

  function flash(text) {
    setMsg(text);
    setTimeout(() => setMsg(''), 3000);
  }

  return (
    <div>
      <h1 style={styles.h1}>Posts</h1>
      <p style={styles.sub}>Search uses query params — <code>GET /api/posts?search=...</code></p>

      {/* SEARCH */}
      <input
        style={{ ...styles.input, marginBottom: '1.5rem', width: '100%' }}
        placeholder="Search posts by title or body…"
        value={search}
        onChange={e => setSearch(e.target.value)}
        // Every keystroke updates "search" state
        // → triggers useEffect([search])
        // → re-fetches with ?search=...
        // That's a live search powered by server-side filtering.
      />

      {msg && <div style={styles.flash}>{msg}</div>}

      {/* CREATE FORM */}
      <form onSubmit={handleCreate} style={{ ...styles.form, flexDirection: 'column' }}>
        <div style={{ display: 'flex', gap: '0.5rem', flexWrap: 'wrap' }}>
          <input style={{ ...styles.input, flex: 2 }} placeholder="Title" value={form.title}  onChange={e => setForm({ ...form, title: e.target.value })} />
          <input style={{ ...styles.input, flex: 1 }} placeholder="Author" value={form.author} onChange={e => setForm({ ...form, author: e.target.value })} />
        </div>
        <div style={{ display: 'flex', gap: '0.5rem' }}>
          <input style={{ ...styles.input, flex: 1 }} placeholder="Body" value={form.body} onChange={e => setForm({ ...form, body: e.target.value })} />
          <button type="submit" style={styles.btn}>Add post</button>
        </div>
      </form>

      {/* POSTS LIST */}
      {loading ? (
        <p style={styles.muted}>Loading…</p>
      ) : posts.length === 0 ? (
        <p style={styles.muted}>No posts found{search ? ` for "${search}"` : ''}.</p>
      ) : (
        <ul style={styles.list}>
          {posts.map(post => (
            <li key={post.id} style={styles.item}>
              <div>
                <div style={{ fontWeight: 'bold', fontSize: '0.95rem' }}>{post.title}</div>
                <div style={styles.muted}>{post.body}</div>
                <div style={{ ...styles.muted, fontSize: '0.8rem' }}>by {post.author} · #{post.id}</div>
              </div>
              <button onClick={() => handleDelete(post.id)} style={styles.delBtn}>delete</button>
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}

const styles = {
  h1:    { fontSize: '1.8rem', fontWeight: 'bold', marginBottom: '0.25rem' },
  sub:   { color: '#666', fontSize: '0.88rem', marginBottom: '1rem' },
  flash: { background: '#e8f5e9', border: '1px solid #a5d6a7', padding: '0.5rem 0.75rem', borderRadius: '4px', marginBottom: '1rem', fontSize: '0.9rem' },
  form:  { display: 'flex', gap: '0.5rem', marginBottom: '1.5rem', flexWrap: 'wrap' },
  input: { padding: '0.4rem 0.75rem', border: '1px solid #ddd', borderRadius: '4px', fontSize: '0.9rem' },
  btn:   { padding: '0.4rem 1rem', background: '#1a1a1a', color: '#fff', border: 'none', borderRadius: '4px', cursor: 'pointer', fontSize: '0.9rem', whiteSpace: 'nowrap' },
  list:  { listStyle: 'none', display: 'flex', flexDirection: 'column', gap: '0.5rem' },
  item:  { display: 'flex', justifyContent: 'space-between', alignItems: 'center', padding: '0.75rem 1rem', border: '1px solid #eee', borderRadius: '6px', background: '#fff', gap: '1rem' },
  muted: { color: '#888', fontSize: '0.88rem' },
  delBtn:{ background: 'none', border: '1px solid #ddd', borderRadius: '4px', padding: '2px 8px', cursor: 'pointer', fontSize: '0.8rem', color: '#888', flexShrink: 0 },
};

export default PostsPage;
