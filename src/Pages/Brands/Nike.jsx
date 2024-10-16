import React from 'react'
import './Nike.css';
import { nike } from "../../showcase";
import { Item } from "../Item"

export const Nike = (props) => {
  return (
    <div className="eachShoe">
      <h2>Nike</h2>
      <div className="shoe-showcase">
        {nike.map((shoe,i)=>{
          return <Item key={i} id={shoe.id} name={shoe.name} image={shoe.image} price={shoe.price}/>
        })}
      </div>
    </div>
  )
}
