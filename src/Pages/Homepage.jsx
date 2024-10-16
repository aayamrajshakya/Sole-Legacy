import React from 'react'
import "./Homepage.css";
import { HomepageShowcase } from './HomepageShowcase'
export const Homepage = () => {
  return (
    <div className="background">
        <img src="/Assets/banner.png" className="banner"/>
        <div className = "first-statement">Introducing our all new Nike A100...</div>
        <div className="second-statement">...where style meets performance, and every step feels like a runway walk!</div>
        <div className='button-container'>
        <div className="button-85">
          <div>Buy now!</div>
        </div>
        </div>
        <HomepageShowcase />
    </div>
  )
}
