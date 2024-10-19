// https://medium.com/geekculture/how-to-use-react-router-useparams-436851fd5ef6

import React from 'react'
import "./IndivShoe.css"
import { showcase, women, men } from "../../shoeInventory"
import { useParams } from 'react-router-dom'

export const IndivShoe = () => {
    const { url } = useParams();
    let allShoes = [...women,...men]
  return (
    <div className="item">
        {allShoes.filter(shoe => shoe.url === url).map((shoe, index) =>(
            <div key={index}>
            <div className="image">
                <img src = {shoe.image} />
            </div>
            <div className="text_info">
                <p>{shoe.name}</p>
                <p>${shoe.price}</p>
                <p>{shoe.description}</p>
            </div>
            </div>
                
        ))}
    </div>
  )
}
