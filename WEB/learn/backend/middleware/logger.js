// ═══════════════════════════════════════════════════════════
//  middleware/logger.js  —  WHAT IS MIDDLEWARE?
//
//  Middleware is any function with this exact signature:
//    (req, res, next) => { ... }
//
//  It sits BETWEEN the incoming request and your route handler.
//  The "next" function passes control to whatever comes next
//  in the chain (the next middleware or the route handler).
//
//  If you never call next(), the request hangs forever.
//  Always call next() unless you're sending a response yourself.
// ═══════════════════════════════════════════════════════════

function logger(req, res, next) {
  const time   = new Date().toLocaleTimeString();
  const method = req.method; // GET, POST, PUT, DELETE
  const url    = req.url;    // /api/users, /api/posts/1, etc.

  console.log(`[${time}]  ${method}  ${url}`);

  next(); // IMPORTANT: pass control to the next step
}

module.exports = logger;
