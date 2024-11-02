// https://stackoverflow.com/a/27976676/23011800

import React from 'react';
import "./Register.css";
import { Link } from "react-router-dom";

export const Register = () => {
  return (
    <div className="page_header">
      <div className="register">
        <div className="login_box">
          <div className="storeName">
            <h3>Sign Up</h3>
          </div>
          <div className="form">
            <form>
              <label>
                <input type="email" placeholder="E-mail" required />
              </label>
              <label>
                <input id="password" name="password" type="password" pattern="^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#$%^&*_=+-]).{8,12}$" placeholder="Password" required />
              </label>
              <label>
                <input id="password_two" name="password_two" type="password" pattern="^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#$%^&*_=+-]).{8,12}$" placeholder="Confirm Password" required />
              </label>
              <div className="role_selection">
                <label className="radio-inline">
                  <input type="radio" name="optradio" defaultChecked /> Buyer
                </label>
                <label className="radio-inline">
                  <input type="radio" name="optradio" /> Seller
                </label>
                <label className="radio-inline">
                  <input type="radio" name="optradio" /> Admin
                </label>
              </div>
              <label>
                <input type="text" placeholder="Address" required />
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