import React from 'react';
import { Link, useNavigate } from "react-router-dom";
import axios from 'axios';

export const Logout = () => {
  const navigate = useNavigate();

  const handleLogout = async () => {
    try {
      const response = await axios.get('http://localhost:5000/logout', {
        withCredentials: true, // Sends cookies with the request
      });
      alert(response.data.message || "Successfully logged out");
      navigate("/"); 
    } catch (error) {
      alert(error.response?.data?.error || "Flask server offline");
    }
  };

  return (
    <div className="page_header">
      <div className="login">
        <div className="login_box">
          <div className="storeName">
            <h3>Logout</h3>
          </div>
        </div>
        <div className="bottom_text">
          <button onClick={handleLogout}>Logout</button>
          New user? <Link to="/register">Sign Up</Link>
        </div>
      </div>
    </div>
  );
};
