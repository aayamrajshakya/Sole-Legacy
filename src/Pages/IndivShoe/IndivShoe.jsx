// https://medium.com/geekculture/how-to-use-react-router-useparams-436851fd5ef6

import React from 'react'
import "./IndivShoe.css"
import { useParams } from 'react-router-dom'

export const IndivShoe = (props) => {
  return (
    <div className="item">
        <div className="image">
            <img src={props.image}/>
        </div>
        <p>Sabbai jutta haru</p>
        <p>${props.price} / ${props.price}</p>

    </div>
  )
}
