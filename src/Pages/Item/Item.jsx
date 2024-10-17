import React from 'react'
import './Item.css'

export const Item = (props) => {
  return (
    <div className="item">
        <div className="image">
            <img src={props.image}/>
        </div>
        <p>{props.name}</p>
        <p>${props.price}</p>

    </div>
  )
}
