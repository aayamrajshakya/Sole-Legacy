import React from 'react';
import "./Login.css";
import { Link } from "react-router-dom";

export const Login = () => {
  return (
    <div className="page_header">
      <div className="login">
        <div className="login_box">
          <div className="storeName">
            <h3>Login</h3>
          </div>
          <div className="form">
            <form>
              <label>
                <input type="email" placeholder="E-mail" required />
              </label>
              <label>
                <input type="password" placeholder="Password" required />
              </label>
              <div>
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