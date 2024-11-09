import React, { useState, useEffect } from "react";
import './Cart.css';
import axios from 'axios';
import { Link, useNavigate } from 'react-router-dom';
import login_icon from "../../Components/Assets/general/login.png";

export const Cart = () => {
  const [isLoggedIn, setIsLoggedIn] = useState(false);

    const navigate = useNavigate();

    useEffect(() => {
      checkLoginStatus();
    }, []);
  
    const checkLoginStatus = async () => {
      try {
        const response = await axios.get('http://localhost:5000/dashboard', {
          withCredentials: true
        });
        setIsLoggedIn(true);
      } catch (error) {
        setIsLoggedIn(false);
      }
    };
  
    return (
      <div className="cart_page">
        {isLoggedIn ? (
          <h3>Cart</h3>
        ) : (
          <>
            <h3>This page is inaccessible!</h3>
            <h4>Please log in and come back.</h4>
            <Link to="/login"><button class="action_btn" role="button">Log in <img src={login_icon} /></button></Link>
          </>
        )}
      </div>
    )
  };