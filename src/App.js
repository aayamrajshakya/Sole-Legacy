import React from 'react';
import './App.css';
import Footer from "./Components/Footer";
import { NavBar } from './Components/NavBar/NavBar';
import { Homepage } from './Pages/Homepage';
import { Men } from './Pages/Men';
import { Women } from './Pages/Women';
import { BrowserRouter, Routes, Route } from 'react-router-dom';

function App() {
  return (
    <div className="App">
      <BrowserRouter>
      <NavBar />
      <Routes>
        <Route path='/' element={<Homepage/>}/>
        <Route path='/women' element={<Women/>}/>
        <Route path='/men' element={<Men/>}/>
      </Routes>
      </BrowserRouter>
      <Footer />
    </div>
  );
}

export default App;