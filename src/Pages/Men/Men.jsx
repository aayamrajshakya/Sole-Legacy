import React from 'react'
import { men } from "../../shoeInventory"
import "./Men.css"
import { Item } from "../Item/Item"


export const Men = (props) => {
  return (
    <div className="men-shoe">
      <h2>Men's collection</h2>
      <div className="men-catalog">
      {men.map((shoe,i)=>{
          return <Item key={i} id={shoe.id} name={shoe.name} image={shoe.image} price={shoe.price}/>
        })}
      </div>
    </div>
  )
}
