import React from 'react'
import './HomepageShowcase.css';
import showcase from "../showcase";
import { Item } from "./Item"

export const HomepageShowcase = (props) => {
  return (
    <div className="eachShoe">
      <h2>Our best sellers</h2>
      <div className="shoe-showcase">
        {showcase.map((shoe,i)=>{
          return <Item key={i} id={shoe.id} name={shoe.name} image={shoe.image} price={shoe.price}/>
        })}
      </div>
    </div>
  )
}
