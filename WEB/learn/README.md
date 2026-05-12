# webdev-learn

A minimal full-stack site that teaches web development through its own code.
Every file is heavily commented — the comments ARE the lesson.

## Structure

```
webdev-learn/
├── backend/                   ← Node.js + Express server
│   ├── index.js               ← Entry point. Registers middleware & routes.
│   ├── package.json           ← Dependencies (express, cors)
│   ├── middleware/
│   │   └── logger.js          ← What middleware is & how to write one
│   └── routes/
│       ├── users.js           ← Full CRUD + route params explained
│       └── posts.js           ← Query params + filtering explained
│
└── frontend/                  ← React app (Vite)
    ├── index.html             ← Only HTML file — React mounts here
    ├── vite.config.js         ← What Vite is & why we need it
    ├── package.json           ← Dependencies (react, react-router-dom)
    └── src/
        ├── main.jsx           ← React entry point, BrowserRouter setup
        ├── App.jsx            ← Routes definition, layout
        ├── index.css          ← Global styles
        ├── components/
        │   └── Navbar.jsx     ← Reusable component, useLocation hook
        └── pages/
            ├── Home.jsx       ← Props, static rendering
            ├── UsersPage.jsx  ← useState, useEffect, fetch, full CRUD
            ├── PostsPage.jsx  ← Query params, functional state updates
            └── ConceptsPage.jsx ← Glossary of every concept
```

## How to run

### 1. Start the backend
```bash
cd backend
npm install
node index.js
# Server runs on http://localhost:3001
```

### 2. Start the frontend (in a new terminal)
```bash
cd frontend
npm install
npm run dev
# React app runs on http://localhost:5173
```

### 3. Open the app
Visit http://localhost:5173 in your browser.

## What each page shows

| Page      | Concept demonstrated                              |
|-----------|---------------------------------------------------|
| Home      | Components, props, layout                         |
| Users     | useState, useEffect, fetch, POST, DELETE          |
| Posts     | Query params, search, functional state updates    |
| Concepts  | Glossary — every term explained plainly           |

## Concepts covered (read files in this order)

1. `backend/index.js`        — what a server is, middleware, routing
2. `backend/middleware/logger.js` — what middleware is
3. `backend/routes/users.js` — REST, route params, req/res, status codes
4. `backend/routes/posts.js` — query params, filtering
5. `frontend/src/main.jsx`   — React entry, BrowserRouter
6. `frontend/src/App.jsx`    — JSX, components, routing
7. `frontend/src/pages/UsersPage.jsx` — useState, useEffect, fetch
8. `frontend/src/pages/PostsPage.jsx` — reactive search, functional updates
