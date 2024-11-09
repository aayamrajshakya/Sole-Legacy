import React from 'react';
import './App.css';
import Footer from "./Components/Footer/Footer";
import { NavBar } from './Components/NavBar/NavBar';
import { Homepage } from './Pages/Homepage/Homepage';
import { Men } from './Pages/Men/Men';
import { Women } from './Pages/Women/Women';
import { Login } from './Pages/Authentication/Login';
import { Register } from './Pages/Register/Register';
import { Cart } from './Pages/Cart/Cart';
import { Wishlist } from './Pages/Wishlist/Wishlist';
import { IndivShoe } from './Pages/IndivShoe/IndivShoe';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import { Dashboard } from './Pages/Authentication/Dashboard';
import { PageNotFound } from './Components/PageNotFound/PageNotFound';
import { Search } from './Pages/Search/Search';

function App() {
  return (
    <div className="App">
      <BrowserRouter>
      <NavBar />
      <Routes>
        <Route path='/' element={<Homepage/>}/>
        <Route path='/women' element={<Women/>}/>
        <Route path='/women/:url' element={<IndivShoe/>}/>
        <Route path='/men' element={<Men/>}/>
        <Route path='/men/:url' element={<IndivShoe/>}/>
        <Route path='/login' element={<Login/>}/>
        <Route path='/register' element={<Register/>}/>
        <Route path='/cart' element={<Cart/>}/>
        <Route path='/wishlist' element={<Wishlist/>}/>
        <Route path='/dashboard' element={<Dashboard/>}/>
        <Route path='/search' element={<Search/>}/>
        <Route path="*" element={<PageNotFound />} />
      </Routes>
      </BrowserRouter>
      <Footer />
    </div>
  );
}

export default App;
