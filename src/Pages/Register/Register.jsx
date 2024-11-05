// Password validation: https://stackoverflow.com/a/27976676/23011800
// Special thanks to: https://medium.com/@yasmeen.yousef05/authentication-in-react-app-with-flask-server-sided-sessions-e97006db749e

import React, { useState } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import "./Register.css";
import axios from "axios";

export const Register = () => {
  const [fullName, setFullName] = useState('');
  const [email, setEmail] = useState('');
  const [plain_password, setPassword] = useState('');
  const [plain_confirmPassword, setConfirmPassword] = useState('');
  const [address, setAddress] = useState('');
  const [usertype, setUserType] = useState('Buyer');

  const navigate = useNavigate();

  // explanation: https://stackoverflow.com/questions/50320055/react-handlesubmit-with-axios-post-with-e-preventdefault-still-refreshes
  const handleSubmit = async (e) => {
    e.preventDefault();
  
    if (plain_password !== plain_confirmPassword) {
      alert("Passwords do not match");
      return;
    }
  
    const data = { fullName, email, plain_password, address, usertype };
  
    try {
      const response = await axios.post('http://localhost:5000/register', data, {
          headers: {
              'Content-Type': 'application/json',
          },
          withCredentials: true,
      });
      alert(response.data.message);
      navigate("/login");  // user will be taken to login page once successfully registered
  } catch (error) {
    alert(error.response?.data?.error || "Flask server offline");
  }
};

  return (
    <div className="page_header">
      <div className="register">
        <div className="login_box">
          <div className="storeName">
            <h3>Sign Up</h3>
          </div>
          <div className="form">
            <form onSubmit={handleSubmit}>
              <label>
                <input type="text" placeholder="Full Name" value={fullName} onChange={(e) => setFullName(e.target.value)} required />
              </label>
              <label>
                <input type="email" placeholder="E-mail" value={email} onChange={(e) => setEmail(e.target.value)} required />
              </label>
              <label>
                <input id="password" name="password" type="password" pattern="^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#$%^&*_=+-]).{8,12}$" placeholder="Password" value={plain_password} onChange={(e) => setPassword(e.target.value)} required />
              </label>
              <label>
                <input id="password_two" name="password_two" type="password" pattern="^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#$%^&*_=+-]).{8,12}$" placeholder="Confirm Password" value={plain_confirmPassword} onChange={(e) => setConfirmPassword(e.target.value)} required />
              </label>
              <div className="role_selection">
                <label className="radio-inline">
                  <input type="radio" name="optradio" value="Buyer" checked={usertype === 'Buyer'} onChange={(e) => setUserType(e.target.value)} /> Buyer
                </label>
                <label className="radio-inline">
                  <input type="radio" name="optradio" value="Seller" checked={usertype === 'Seller'} onChange={(e) => setUserType(e.target.value)} /> Seller
                </label>
                <label className="radio-inline">
                  <input type="radio" name="optradio" value="Admin" checked={usertype === 'Admin'} onChange={(e) => setUserType(e.target.value)} /> Admin
                </label>
              </div>
              <label>
                <input type="text" placeholder="Address" value={address} onChange={(e) => setAddress(e.target.value)} required />
              </label>
              <div>
                <button type="submit">Sign Up</button>
              </div>
            </form>
          </div>
          <div className="bottom_text">
            Have an account? <Link to="/login">Sign In</Link>
          </div>
        </div>
      </div>
    </div>
  );
};