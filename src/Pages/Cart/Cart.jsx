import React, { useState, useEffect } from "react";
import './Cart.css';
import axios from 'axios';
import { Link } from 'react-router-dom';
import { Item } from "../Item/Item";
import login_icon from "../../Components/Assets/general/login.png";

export const Cart = () => {
  const [isLoggedIn, setIsLoggedIn] = useState(false);
  const [cartItems, setCartItems] = useState([]);
  const [total, setTotal] = useState(0);
  const [error, setError] = useState(null);
  

  useEffect(() => {
    checkLoginStatus();
  }, []);

  const checkLoginStatus = async () => {
    try {
      const response = await axios.get('http://localhost:5000/dashboard', {
        withCredentials: true
      });
      setIsLoggedIn(true);
      fetchCartItems();
    } catch (error) {
      setIsLoggedIn(false);
    }
  };

  const fetchCartItems = async () => {
    try {
      const response = await axios.get('http://localhost:5000/cart/items', {
        withCredentials: true
      });
      setCartItems(response.data.items);
      setTotal(response.data.total);
    } catch (error) {
      setError(error.response?.data?.error || "Failed to fetch cart items");
    }
  };

  const updateQuantity = async (itemId, newQuantity) => {
    try {
      await axios.put('http://localhost:5000/cart/update', {
        itemId,
        quantity: newQuantity
      }, {
        withCredentials: true
      });
      fetchCartItems();
    } catch (error) {
      setError(error.response?.data?.error || "Failed to update quantity");
    }
  };

  const removeItem = async (itemId) => {
    try {
      await axios.post('http://localhost:5000/cart/remove', {
        itemId
      }, {
        withCredentials: true
      });
      fetchCartItems(); 
    } catch (error) {
      setError(error.response?.data?.error || "Failed to remove item");
    }
  };

  if (!isLoggedIn) {
    return (
      <div className="cart_page">
        <h3>This page is inaccessible!</h3>
        <h4>Please log in and come back.</h4>
        <Link to="/login"><button className="cartOG_btn">Log in <img src={login_icon} alt="Login" /></button></Link>
      </div>
    );
  }

  return (
    <div className="cart_page">
      <h3>Shopping Cart</h3>
      
      {cartItems.length === 0 ? (
        <div className="empty_cart">
          <p>Your cart is empty</p>
          <Link to="/">
            <button className="action_btn">Continue Shopping</button>
          </Link>
        </div>
      ) : (
        <>
          <div className="cart_items">
            {cartItems.map((item) => (
              <div key={item.itemId} className="cart_item">
                <div className="cart_item_image">
                  <Item 
                    id={item.itemId}
                    name={item.name}
                    image={item.image}
                    price={item.price}
                    gender={item.gender}
                  />
                </div>

                <div className="cart_item_actions">
                  <div className="quantity_control">
                    <button 
                      className="quantity_button"
                      onClick={() => updateQuantity(item.itemId, item.quantity - 1)}
                      disabled={item.quantity <= 1}
                    >
                      -
                    </button>
                    <span>{item.quantity}</span>
                    <button 
                      className="quantity_button"
                      onClick={() => updateQuantity(item.itemId, item.quantity + 1)}
                    >
                      +
                    </button>
                  </div>
                  
                  <button 
                    className="action_btn"
                    onClick={() => removeItem(item.itemId)}
                  >
                    Remove
                  </button>
                </div>
              </div>
            ))}
          </div>

          <div className="cart_summary">
            <h3>Cart Summary</h3>
            <p>Total: ${total.toFixed(2)}</p>
            <Link to="/checkout">
              <button className="action_btn">Continue To Checkout</button>
            </Link>
          </div>
        </>
      )}
    </div>
  );
};