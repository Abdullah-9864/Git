// ═══════════════════════════════════════════════════════════
//  src/App.jsx  —  ROUTING & LAYOUT
//
//  This component does two things:
//    1. Defines all the routes (URL → component mapping)
//    2. Wraps every page in a shared layout (Navbar + content)
//
//  WHAT IS A COMPONENT?
//  A component is just a function that returns JSX (HTML-like syntax).
//  React calls your function, gets the JSX, and renders it to the DOM.
//  Components start with a capital letter by convention.
//
//  WHAT IS JSX?
//  JSX looks like HTML but it compiles to JavaScript.
//  <div className="box"> becomes React.createElement('div', {className:'box'})
//  You write className instead of class (class is a reserved JS keyword).
// ═══════════════════════════════════════════════════════════

import { Routes, Route } from 'react-router-dom';
import Navbar    from './components/Navbar';
import Home      from './pages/Home';
import UsersPage from './pages/UsersPage';
import PostsPage from './pages/PostsPage';
import ConceptsPage from './pages/ConceptsPage';

// styles object — CSS-in-JS (inline styles as a plain object)
// Alternative to writing a separate CSS file for this component.
const styles = {
  layout:  { minHeight: '100vh', display: 'flex', flexDirection: 'column' },
  content: { flex: 1, maxWidth: '860px', margin: '0 auto', padding: '2rem 1.5rem', width: '100%' },
};

function App() {
  return (
    <div style={styles.layout}>
      <Navbar />

      <main style={styles.content}>
        {/*
          Routes: looks at the current URL and renders the matching component.
          Route path="/" is the homepage.
          Route path="/users" renders UsersPage, etc.

          This all happens CLIENT-SIDE — no server request is made
          when you click a link. React Router swaps the component instantly.
        */}
        <Routes>
          <Route path="/"         element={<Home />}        />
          <Route path="/users"    element={<UsersPage />}   />
          <Route path="/posts"    element={<PostsPage />}   />
          <Route path="/concepts" element={<ConceptsPage />} />
        </Routes>
      </main>
    </div>
  );
}

export default App;
// export default = this is the "main" export of the file.
// Other files import it with:  import App from './App'
