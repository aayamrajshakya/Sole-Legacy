import React from 'react'
import "./Women.css"
import { women } from "../../shoeInventory"
import { BrowserRouter as Router, Route, Link } from "react-router-dom";
import { Item } from "../Item/Item"

export const Women = () => {
  return (
    <div className="women-shoe">
      <h2>Women's collection</h2>
      <div className="women-catalog">
      {women.map((shoe,i)=>(
        <Link to={`${shoe.name}`}>
        <Item key={i} id={shoe.id} name={shoe.name} image={shoe.image} price={shoe.price}/>
        </Link>
        ))}
      </div>
    </div>
  )
}
