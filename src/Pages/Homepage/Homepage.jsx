import React from 'react'
import "./Homepage.css";
import { HomepageShowcase } from '../HomepageShowcase/HomepageShowcase'
import banner from '../../Components/Assets/general/banner.jpg'
export const Homepage = () => {
  return (
    <div className="background">
        <img src={banner} className="banner"/>
        <div className = "first-statement">Introducing our all new Nike A100...</div>
        <div className="second-statement">Life is too short for bad shoes!</div>
        <div className='button-container'>
        <div className="button-85">
          <div>Buy now!</div>
        </div>
        </div>
        <HomepageShowcase />
    </div>
  )
}
