import React from 'react'
import "./Homepage.css";
import { HomepageShowcase } from '../HomepageShowcase/HomepageShowcase'
import { BrowserRouter as Router, Route, Link } from "react-router-dom";
import banner from '../../Components/Assets/general/banner.jpg'

export const Homepage = () => {
  return (
    <div className="background">
      <img src={banner} className="banner" />
      <div className="first-statement">Introducing our all new Nike Air Jordan 1...</div>
      <div className="second-statement">Life is too short for bad shoes!</div>
      <div className='button-container'>
        <Link to={`men/Nike_Air_Jordan_1`}>
          <div className="button-85">
            <div className="button-text">Buy now!</div>
          </div>
          <div></div>
        </Link>
      </div>
      <HomepageShowcase />
    </div>
  )
}
