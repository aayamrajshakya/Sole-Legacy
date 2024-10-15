import React from 'react'
import banner from '../Components/Assets/banner.png';
import "./Homepage.css";

export const Homepage = () => {
  return (
    <div className="background">
        <img src={banner} className="banner"/>
        <h3>Nike's quality at Temu's price</h3>
    </div>
  )
}
