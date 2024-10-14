import React from 'react'
import "./NavBar.css";
import logo from '../Assets/banner_logo.png';

export const NavBar = () => {
  return (
    <div className='navbar'>
        <div className='nav-logo'>
            <h2>Sole Legacy</h2>
        </div>
        <ul className="nav-menu">
            <li>Women</li>
            <li>Men</li>
            <li>Kids</li>
            <li>Home</li>
        </ul>
        <div className="nav-login-cart">
            <button>Login</button>
        </div>
    </div>
  )
}
