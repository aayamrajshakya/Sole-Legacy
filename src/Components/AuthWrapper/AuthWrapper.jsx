import React, { useEffect, useState } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import login_icon from "../Assets/general/login.png"

const AuthWrapper = ({ children, fallback }) => {
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
  }

  if (!isLoggedIn) {
    return fallback || (
      <div>
        <h3>This page is unaccessible!</h3>
        <h4>Please log in and come back.</h4>
        <Link to="/login"><button class="action_btn" role="button">Log in <img src={login_icon} /></button></Link>
      </div>
    );
  }

  return children;
};

export default AuthWrapper;