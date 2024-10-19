import React from 'react'
import './HomepageShowcase.css';
import showcase from "../../shoeInventory";
import { BrowserRouter as Router, Route, Link } from "react-router-dom";
import { Item } from "../Item/Item"

export const HomepageShowcase = (props) => {
  return (
    <div className="eachShoe">
      <h2>Our best sellers</h2>
      <div className="shoe-showcase">
        {showcase.map((shoe,i)=>(
          <Link to={`men/${shoe.url}`}>
          <Item key={i} id={shoe.id} name={shoe.name} image={shoe.image} price={shoe.price}/>
          </Link>
        ))}
      </div>
    </div>
  )
}
