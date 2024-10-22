// https://www.w3schools.com/react/react_forms.asp

import React from 'react'
import "./Register.css"
import { BrowserRouter as Router, Route, Link } from "react-router-dom";

export const Register = () => {
  return (
    <div className="page_header">
      <div className="login_box">
        <div className="storeLogo">
          <h2>Register</h2>
        </div>
      {/* Kevin, your registration form goes here      */}
      <input className="text_box" placeholder="E-mail address" id="email" value="" />
      <input className="text_box" placeholder="Full name" id="fullName" value="" />
      <input className="text_box" placeholder="Phone number" id="phoneNumber" value="" />
      <input className="text_box" placeholder="Password" id="password" value="" />
      <div className="bottom_text">
      <Link to ="/login">Already have an account?</Link>
      </div>
      
      </div>
      
    </div>
  )
}

