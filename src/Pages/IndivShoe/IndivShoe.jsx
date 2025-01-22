import React, { useEffect, useState } from 'react';
import axios from 'axios';
import "./IndivShoe.css";
import { useParams } from 'react-router-dom';
import addToCart from "../../Components/Assets/general/addtocart.png";
import wishlist from "../../Components/Assets/general/wishlist.png";

export const IndivShoe = () => {
    const { url } = useParams();
    const [shoe, setShoe] = useState(null);
    const [shoeSize, setShoeSize] = useState('9');                  // default shoe size if not selected anything
    const [shoeColor, setShoeColor] = useState('White');            // default shoe color if not selected anything

    const addToWishlist = async () => {
        try {
            const response = await axios.post('http://localhost:5000/addToWishlist', {
                ItemName: shoe.ItemName,
                Price: shoe.Price,
                Color: shoeColor,
                Size: shoeSize,
                Gender: shoe.Gender,
                Slug: shoe.Image
            }, {
                withCredentials: true
            });
            alert(response.data.message);
        } catch (error) {
            alert(error.response?.data?.error || "Flask server offline");
        }
    };

    const handleAddToCart = async () => {
        try {
            const response = await axios.post('http://localhost:5000/cart/add', {
                itemName: shoe.ItemName,
                quantity: 1  // You could add a quantity selector if needed
            }, {
                withCredentials: true  // Important for session handling
            });
            alert(response.data.message);
        } catch (error) {
            if (error.response?.status === 401) {
                alert("Log in first!");
            } else {
                alert(error.response?.data?.error || "Failed to add item to cart");
            }
        }
    };

    useEffect(() => {
        const fetchShoeData = async () => {
            try {
                const response = await axios.get(`http://localhost:5000/shoe/${url}`);
                setShoe(response.data);
            } catch (error) {
                alert(error.response?.data?.error || "Flask server offline");
            }
        };
        fetchShoeData();
    }, [url]);

    if (!shoe) {
        return null; // Show a loading message while fetching data
    }

    return (
        <div className="main_div">
            <div className="indivShoePage">
                <div className="indivShoe_img">
                    <img src={`${process.env.PUBLIC_URL}/${shoe.Gender}/${shoe.Image}`} />
                </div>
                <div className="indivShoe_info">
                    <h3>{shoe.ItemName}
                        <div className="special_offer">{shoe.ItemName === "Nike Air Jordan 1" ? "Old price: $179" : ""}<div className="price">${shoe.Price} </div>
                        </div>
                    </h3>
                    <h3>Description <div className="description">{shoe.Description}</div></h3>
                    <div className="dropdown_menus">
                        <label for="shoeSize">Size: </label>
                        <select name="size" id="size" value={shoeSize} onChange={(e) => setShoeSize(e.target.value)}>
                            <option value="8">{shoe.Gender === "women" ? "8 F" : "8 M"}</option>
                            <option value="8.5">{shoe.Gender === "women" ? "8.5 F" : "8.5 M"}</option>
                            <option value="9" selected>{shoe.Gender === "women" ? "9 F" : "9 M"}</option>
                            <option value="9.5">{shoe.Gender === "women" ? "9.5 F" : "9.5 M"}</option>
                            <option value="10">{shoe.Gender === "women" ? "10 F" : "10 M"}</option>
                            <option value="10.5">{shoe.Gender === "women" ? "10.5 F" : "10.5 M"}</option>
                            <option value="11">{shoe.Gender === "women" ? "11 F" : "11 M"}</option>
                        </select>

                        <label for="shoeColor">Color: </label>
                        <select name="color" id="color" value={shoeColor} onChange={(e) => setShoeColor(e.target.value)}>
                            <option value="White">White</option>
                            <option value="Yellow">Yellow</option>
                            <option value="Green">Green</option>
                            <option value="Blue">Blue</option>
                            <option value="Grey">Grey</option>
                        </select>
                    </div>

                    <button onClick={handleAddToCart} class="button-35">Add to cart <img src={addToCart} /></button>
                    <button onClick={addToWishlist} class="button-35">Favorite<img className="wishlist" src={wishlist} /></button>
                </div>
            </div>
        </div>
    );
};
