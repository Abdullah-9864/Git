// ═══════════════════════════════════════════════════════════
//  src/main.jsx  —  REACT ENTRY POINT
//
//  This is where React starts. It mounts the entire app
//  into the <div id="root"> in index.html.
//
//  BrowserRouter wraps everything so React Router can work.
//  React Router = client-side routing. It makes the URL change
//  without the browser making a new request to the server.
//  /users, /posts — all handled by JavaScript in the browser.
// ═══════════════════════════════════════════════════════════

import React from 'react';
import ReactDOM from 'react-dom/client';
import { BrowserRouter } from 'react-router-dom';
import App from './App';
import './index.css';

ReactDOM.createRoot(document.getElementById('root')).render(
  <BrowserRouter>
    <App />
  </BrowserRouter>
);
