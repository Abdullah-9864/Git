// ═══════════════════════════════════════════════════════════
//  index.js  —  THE ENTRY POINT
//
//  This is the first file Node.js runs.
//  Think of it as the "main()" of your entire server.
//  Run it with:  node index.js
//  Auto-reload:  nodemon index.js
// ═══════════════════════════════════════════════════════════

const express = require('express'); // import the Express library
const cors    = require('cors');    // import CORS middleware

// Import our route files (each file handles one "resource")
const usersRouter = require('./routes/users');
const postsRouter = require('./routes/posts');

const app  = express(); // create the Express application
const PORT = 3001;      // port this server listens on

// ── MIDDLEWARE ───────────────────────────────────────────
// Middleware = a function that runs on EVERY request
// BEFORE it reaches your route handler.
// You register middleware with app.use().
// Order matters — they run top to bottom.

app.use(cors());
// CORS (Cross-Origin Resource Sharing):
// Browsers block requests from one origin (localhost:5173)
// to another (localhost:3001) by default — it's a security rule.
// This middleware tells the browser: "it's okay, allow it."

app.use(express.json());
// Parses the JSON body of incoming requests.
// Without this, req.body would always be undefined.
// Now when a POST sends { "name": "Abdullah" }, you can read it.

app.use(require('./middleware/logger'));
// Our custom middleware — logs every request to the console.
// This runs before every route. See middleware/logger.js.

// ── ROUTES ──────────────────────────────────────────────
// We "mount" routers at a base path.
// Every route inside usersRouter is prefixed with /api/users.
// Every route inside postsRouter is prefixed with /api/posts.

app.use('/api/users', usersRouter);
app.use('/api/posts', postsRouter);

// ── ROOT ROUTE ───────────────────────────────────────────
// A simple health-check. Visit http://localhost:3001 to confirm
// the server is alive.
app.get('/', (req, res) => {
  res.json({
    message: 'Hello World — the API is alive!',
    tip: 'Try GET /api/users or GET /api/posts'
  });
});

// ── 404 HANDLER ──────────────────────────────────────────
// If NO route above matched the request, Express falls through
// to this catch-all. Always put it last.
app.use((req, res) => {
  res.status(404).json({ error: 'Route not found' });
});

// ── GLOBAL ERROR HANDLER ─────────────────────────────────
// When any route calls next(error), Express skips all normal
// middleware and jumps here. The 4-parameter signature is how
// Express recognises this as an error handler.
app.use((err, req, res, next) => {
  console.error('Unhandled error:', err.message);
  res.status(500).json({ error: 'Something went wrong on the server' });
});

// ── START THE SERVER ─────────────────────────────────────
app.listen(PORT, () => {
  console.log(`Server running → http://localhost:${PORT}`);
});
