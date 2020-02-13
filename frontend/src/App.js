import React, { useState, useEffect } from 'react';
import { BrowserRouter } from 'react-router-dom';
import './App.css';
import Bank from './components/Bank';
import NavBar from './components/NavBar';
import Router from './components/Router';


function App() {
  
  
  
  
  
  return (
    <BrowserRouter>
      <div className="App" >
        <NavBar />
        <Router />
      </div>
    </BrowserRouter>
  );
}

export default App;
