// ═══════════════════════════════════════════════════════════
//  routes/users.js  —  ROUTES, REST API, ROUTE PARAMS
//
//  A route = HTTP method + URL pattern + handler function.
//  This file handles everything under /api/users.
//
//  REST naming for a "users" resource:
//    GET    /api/users       → list all
//    GET    /api/users/:id   → get one
//    POST   /api/users       → create
//    PUT    /api/users/:id   → update
//    DELETE /api/users/:id   → delete
// ═══════════════════════════════════════════════════════════

const express = require('express');
const router  = express.Router();
// Router = a mini Express app. It only handles routes.
// We export it and mount it in index.js.

// ── IN-MEMORY DATA ───────────────────────────────────────
// We're using a plain array instead of a real database.
// In production you'd swap this with MongoDB or PostgreSQL.
// The data resets every time you restart the server.
let users = [
  { id: 1, name: 'Abdullah', role: 'developer' },
  { id: 2, name: 'Ali',      role: 'designer'  },
  { id: 3, name: 'Sara',     role: 'manager'   },
];
let nextId = 4;

// ── GET /api/users ────────────────────────────────────────
// req = the request  (what the client sent)
// res = the response (what we send back)
router.get('/', (req, res) => {
  res.json(users);
  // res.json() sends JSON and sets Content-Type: application/json
  // Status code defaults to 200 OK
});

// ── GET /api/users/:id ────────────────────────────────────
// :id is a route parameter — a named wildcard in the URL.
// /api/users/1  →  req.params.id === '1'  (always a string)
// /api/users/42 →  req.params.id === '42'
router.get('/:id', (req, res) => {
  const id   = parseInt(req.params.id); // convert string to number
  const user = users.find(u => u.id === id);

  if (!user) {
    // 404 = Not Found — standard when the resource doesn't exist
    return res.status(404).json({ error: 'User not found' });
  }

  res.json(user);
});

// ── POST /api/users ───────────────────────────────────────
// Create a new user. The client sends data in the request body:
//   { "name": "Abdullah", "role": "developer" }
// express.json() middleware (registered in index.js) parses it
// and puts it on req.body.
router.post('/', (req, res) => {
  const { name, role } = req.body; // destructure what we need

  // Basic validation — always validate before saving
  if (!name || !role) {
    // 400 = Bad Request — the client sent invalid data
    return res.status(400).json({ error: 'name and role are required' });
  }

  const newUser = { id: nextId++, name, role };
  users.push(newUser);

  // 201 = Created — more specific than 200 when you create something
  res.status(201).json(newUser);
});

// ── PUT /api/users/:id ────────────────────────────────────
// Update an existing user. Client sends the fields to change.
// PUT = replace/update. PATCH = partial update (same idea, stricter REST).
router.put('/:id', (req, res) => {
  const id   = parseInt(req.params.id);
  const user = users.find(u => u.id === id);

  if (!user) return res.status(404).json({ error: 'User not found' });

  const { name, role } = req.body;
  if (name) user.name = name; // only update fields that were sent
  if (role) user.role = role;

  res.json(user); // send back the updated user
});

// ── DELETE /api/users/:id ────────────────────────────────
// Remove a user from the array.
router.delete('/:id', (req, res) => {
  const id  = parseInt(req.params.id);
  const idx = users.findIndex(u => u.id === id);

  if (idx === -1) return res.status(404).json({ error: 'User not found' });

  users.splice(idx, 1); // remove 1 element at index idx
  res.json({ message: `User ${id} deleted` });
});

module.exports = router; // export so index.js can mount it
