// https://medium.com/geekculture/how-to-use-react-router-useparams-436851fd5ef6

import React from 'react'
import "./Men.css"
import { men } from "../../shoeInventory"
import { BrowserRouter as Router, Route, Link } from "react-router-dom";
import { Item } from "../Item/Item"

export const Men = () => {
  return (
    <div className="men-shoe">
      <h2>Men's collection</h2>
      <div className="men-catalog">
        {men.map((shoe,i)=>(
          <Link to={`${shoe.url}`}>
          <Item key={i} id={shoe.id} name={shoe.name} image={shoe.image} price={shoe.price}/>
          </Link>
        ))}
      </div>
    </div>
  )
}
