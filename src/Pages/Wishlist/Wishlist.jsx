// Acknowledging use of gen AI here. Initially, isLoggedIn is set to false.
// When checkLogin status makes a `get` request to dashboard and the request is successful, isLoggedIn is set to true, else false

import React, { useState, useEffect } from "react";
import './Wishlist.css';
import axios from 'axios';
import { Link } from 'react-router-dom';
import login_icon from "../../Components/Assets/general/login.png";
import remove_icon from "../../Components/Assets/general/delete.png"

export const Wishlist = () => {
  const [isLoggedIn, setIsLoggedIn] = useState(false);
  const[wishlistItems, setwishlistItems] = useState([]);   // wishlist is set to empty initially

    useEffect(() => {
      checkLoginStatus();
    }, []);
  
    const checkLoginStatus = async () => {
      try {
        const response = await axios.get('http://localhost:5000/dashboard', {
          withCredentials: true
        });
        setIsLoggedIn(true);
        await fetchWishlist();
      } catch (error) {
        setIsLoggedIn(false);
      }
    };
    
    const fetchWishlist = async () => {
      try {
        const response = await axios.get('http://localhost:5000/wishlist', {
          withCredentials: true
        });
        setwishlistItems(response.data.items);
      } catch (error) {
        alert(error.response?.data?.error || "Flask server offline");
      }
    };

    const removeFromWishlist = async (itemName) => {
      try {
        const response = await axios.post('http://localhost:5000/removeFromWishlist', {ItemName: itemName}, {
            withCredentials: true
        });
        alert(response.data.message);
        } catch (error) {
          alert(error.response?.data?.error || "Flask server offline");
        }
        }
        
  
  return (
    <div className="wishlist_page">
      {isLoggedIn ? (
        <>
          <h3>Wishlist</h3>
          {wishlistItems.length === 0 ? (<p>Your wishlist is empty</p>) : (
            <div className="wishlist_main_container">
              {wishlistItems.map((item) => (
                <div key={item.ItemID}  className="wishlist_view">
                  <img className="item_image" src={`${process.env.PUBLIC_URL}/${item.Gender}/${item.Slug}`} />
                  <p className="item_name"><b>{item.ItemName}</b></p>
                  <div className="item_details">
                  <p className="item_gender"><b>Gender:</b> {item.Gender}</p>  
                  <p className="item_price"><b>Price:</b> ${item.Price}</p>
                  <p className="item_color"><b>Color:</b> {item.Color}</p>
                  <p className="item_size"><b>Size:</b> {item.Size}</p> 
                  <button onClick={() => removeFromWishlist(item.ItemName)} className="delete_btn"><img src={remove_icon}/></button>
                </div>
                </div>
              ))}
            </div>
          )}
        </>  
      ) : (
        <>
          <h3>This page is inaccessible!</h3>
          <h4>Please log in and come back.</h4>
          <Link to="/login"><button className="action_btn" role="button">Log in <img src={login_icon} alt="Login" /></button></Link>
        </>
      )}
    </div>
  );
};