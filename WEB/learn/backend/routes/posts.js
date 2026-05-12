// ═══════════════════════════════════════════════════════════
//  routes/posts.js  —  QUERY PARAMS & A SECOND RESOURCE
//
//  New concept here: QUERY PARAMETERS
//  They come after ? in the URL and are key=value pairs.
//  Example: GET /api/posts?search=hello&author=Abdullah
//           req.query = { search: 'hello', author: 'Abdullah' }
//
//  Route params (:id) identify a specific resource.
//  Query params (?search=) filter or configure the response.
// ═══════════════════════════════════════════════════════════

const express = require('express');
const router  = express.Router();

let posts = [
  { id: 1, title: 'Hello World',         body: 'My very first post.',         author: 'Abdullah' },
  { id: 2, title: 'What is an API?',     body: 'An API is a contract.',       author: 'Ali'      },
  { id: 3, title: 'Why use Express?',    body: 'It keeps things simple.',     author: 'Sara'     },
  { id: 4, title: 'React vs Vanilla JS', body: 'React wins for large UIs.',   author: 'Abdullah' },
];
let nextId = 5;

// ── GET /api/posts  (with optional ?search=) ──────────────
router.get('/', (req, res) => {
  const { search, author } = req.query;

  let result = posts;

  // Filter by search term if provided
  if (search) {
    result = result.filter(p =>
      p.title.toLowerCase().includes(search.toLowerCase()) ||
      p.body.toLowerCase().includes(search.toLowerCase())
    );
  }

  // Filter by author if provided
  if (author) {
    result = result.filter(p =>
      p.author.toLowerCase() === author.toLowerCase()
    );
  }

  res.json(result);
});

// ── GET /api/posts/:id ────────────────────────────────────
router.get('/:id', (req, res) => {
  const post = posts.find(p => p.id === parseInt(req.params.id));
  if (!post) return res.status(404).json({ error: 'Post not found' });
  res.json(post);
});

// ── POST /api/posts ───────────────────────────────────────
router.post('/', (req, res) => {
  const { title, body, author } = req.body;

  if (!title || !body || !author) {
    return res.status(400).json({ error: 'title, body, and author are required' });
  }

  const newPost = { id: nextId++, title, body, author };
  posts.push(newPost);
  res.status(201).json(newPost);
});

// ── DELETE /api/posts/:id ─────────────────────────────────
router.delete('/:id', (req, res) => {
  const idx = posts.findIndex(p => p.id === parseInt(req.params.id));
  if (idx === -1) return res.status(404).json({ error: 'Post not found' });
  posts.splice(idx, 1);
  res.json({ message: `Post ${req.params.id} deleted` });
});

module.exports = router;
