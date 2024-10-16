import React from 'react'
import { women } from "../showcase"
import "./Women.css"
import { Item } from "./Item"


export const Women = (props) => {
  return (
    <div className="women-shoe">
      <h2>Women's collection</h2>
      <div className="women-catalog">
      {women.map((shoe,i)=>{
          return <Item key={i} id={shoe.id} name={shoe.name} image={shoe.image} price={shoe.price}/>
        })}
      </div>
    </div>
  )
}
