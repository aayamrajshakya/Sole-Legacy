import React, { useState } from 'react';
import "./Login.css";
import { Link, useNavigate } from "react-router-dom";
import axios from 'axios';

export const Login = () => {
  const [email, setEmail] = useState('');
  const [plain_password, setPassword] = useState('');
  const [userType, setUserType] = useState('');
  const navigate = useNavigate();

  const handleSubmit = async (e) => {
    e.preventDefault();

    const data = { email, plain_password };

    try {
      const response = await axios.post('http://localhost:5000/login', data, {
        headers: {
          'Content-Type': 'application/json',
        },
        withCredentials: true,
      });
      const regUserType = response.data.regUserType;

      if (regUserType !== userType) {
        alert("Wrong user type!");
        return;
      }

      alert(response.data.message);
      if (regUserType === "Buyer") { navigate("/"); }
      else if (regUserType === "Seller") { navigate("/seller"); }
      else if (regUserType === "Admin") { navigate("/admin"); }
      else { navigate("/"); }
    } catch (error) {
      alert(error.response?.data?.error || "Flask server offline");
    }
  };

  return (
    <div className="page_header">
      <div className="login">
        <div className="login_box">
          <div className="storeName">
            <h3>Login</h3>
          </div>
          <div className="form">
            <form onSubmit={handleSubmit}>
              <label>
                <input type="email" placeholder="E-mail" value={email} onChange={(e) => setEmail(e.target.value)} required />
              </label>
              <label>
                <input type="password" placeholder="Password" value={plain_password} onChange={(e) => setPassword(e.target.value)} required />
              </label>
              <div>
                <div className="role_selection">
                  <label className="radio-inline">
                    <input type="radio" name="optradio" value="Buyer" checked={userType === 'Buyer'} onChange={(e) => setUserType(e.target.value)} /> Buyer
                  </label>
                  <label className="radio-inline">
                    <input type="radio" name="optradio" value="Seller" checked={userType === 'Seller'} onChange={(e) => setUserType(e.target.value)} /> Seller
                  </label>
                  <label className="radio-inline">
                    <input type="radio" name="optradio" value="Admin" checked={userType === 'Admin'} onChange={(e) => setUserType(e.target.value)} /> Admin
                  </label>
                </div>
                <button className="signIn" type="submit">Sign In</button>
              </div>
            </form>
          </div>
          <div className="bottom_text">
            New user? <Link to="/register">Sign Up</Link>
          </div>
        </div>
      </div>
    </div>
  );
};