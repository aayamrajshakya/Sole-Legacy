// https://medium.com/geekculture/how-to-use-react-router-useparams-436851fd5ef6
// https://getcssscan.com/css-buttons-examples

import React from 'react'
import "./IndivShoe.css"
import { showcase, women, men } from "../../shoeInventory"
import { useParams } from 'react-router-dom'
import addToCart from "../../Components/Assets/general/addtocart.png"
import wishlist from "../../Components/Assets/general/wishlist.png"

export const IndivShoe = () => {
    const { url } = useParams();
    let allShoes = [...women,...men]
  return (
    <div className="main_div">
        {allShoes.filter(shoe => shoe.url === url).map((shoe, index) =>(
            <div key={index} className="indivShoePage">
                <div className="indivShoe_img">
                <img src = {shoe.image} />
                </div>
            <div className="indivShoe_info">
                {/* The new edition shoe in showcase will get an additional component: old price */}
                {/* https://codesource.io/blog/how-to-use-ternary-operator-in-react/ */}
                {/* here, I choose its url as a unique identifier */}
                
                <h3>{shoe.name} <div className="special_offer">{shoe.url==="Nike_Air_Jordan_1" ? "Old price: $179" : ""}<div className="price">${shoe.price} </div>
                </div></h3>
                
                <h3>Description <div className="description">{shoe.description}</div></h3>

                <div className="dropdown_menus">
                <label for="shoeSize">Size: </label>
                <select name="size" id="size">
                <option value="8">{shoe.gender==="women" ? "8 F" : "8 M"}</option>
                <option value="8.5">{shoe.gender==="women" ? "8.5 F" : "8.5 M"}</option>
                <option value="9" selected>{shoe.gender==="women" ? "9 F" : "9 M"}</option>
                <option value="9.5">{shoe.gender==="women" ? "9.5 F" : "9.5 M"}</option>
                <option value="10">{shoe.gender==="women" ? "10 F" : "10 M"}</option>
                <option value="10.5">{shoe.gender==="women" ? "10.5 F" : "10.5 M"}</option>
                <option value="11">{shoe.gender==="women" ? "11 F" : "11 M"}</option>
                </select>

                <label for="shoeColor">Color: </label>
                <select name="color" id="color">
                <option value="color1" selected>{shoe.gender==="women" ? "Pink" : "Black"}</option>
                <option value="color2">{shoe.gender==="women" ? "Purple" : "Blue"}</option>
                <option value="color3">{shoe.gender==="women" ? "Golden" : "Green"}</option>
                <option value="color4">White</option>
                <option value="color5">Yellow</option>

                </select>
                </div>

                <button class="button-35" role="button">Add to cart <img src={addToCart} /></button>
                <button class="button-35" role="button">Favorite<img className="wishlist" src={wishlist} /></button>

            </div>
            </div>
        ))}
    </div>
  )
}