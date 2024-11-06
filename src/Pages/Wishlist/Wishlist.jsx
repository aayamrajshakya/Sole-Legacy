// Acknowledging use of gen AI here. Initially, isLoggedIn is set to false.
// When checkLogin status makes a `get` request to dashboard and the request is successful, isLoggedIn is set to true, else false

import React, { useState, useEffect } from "react";
import './Wishlist.css';
import axios from 'axios';
import { Link, useNavigate } from 'react-router-dom';
import login_icon from "../../Components/Assets/general/login.png";

export const Wishlist = () => {
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
      <div className="wishlist_page">
        {isLoggedIn ? (
          <h1>Logged in, hi!</h1>
        ) : (
          <>
            <h3>This page is unaccessible!</h3>
            <h4>Please log in and come back.</h4>
            <Link to="/login"><button class="action_btn" role="button">Log in <img src={login_icon} /></button></Link>

          </>
        )}
      </div>
    )
  };