// vite.config.js  —  WHAT IS VITE?
//
// Vite is a build tool. It does two things:
//   1. Dev mode: serves your React app instantly with hot-reload
//      (changes appear in the browser without refreshing)
//   2. Build mode: bundles all your files into plain HTML/CSS/JS
//      for deployment (npm run build)
//
// Without a build tool, you'd have to manually link every file,
// can't use JSX, can't use imports. Vite handles all of that.

import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';

export default defineConfig({
  plugins: [react()],
  server: {
    port: 5173, // the port your React app runs on in dev
  }
});
