import React from 'react';
import ReactDOM from 'react-dom';
//import * as serviceWorker from './serviceWorker';
import './index.css';
import {
  Route,
  BrowserRouter as Router, Routes
} from 'react-router-dom';
import App from './App';
import Header from './components/Header';
import Footer from './components/Footer';


const routing = (
  <Router>
    <React.StrictMode>
      <Header />
      <div>HUETA</div>
      <Routes>
        <Route exact path="/" component={<App />} />
      </Routes>
      <Footer />
    </React.StrictMode>
  </Router>
);

const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(routing);