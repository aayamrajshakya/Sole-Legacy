import React, { useState, useEffect } from 'react';
import "./Women.css";
import { Link } from "react-router-dom";
import { Item } from "../Item/Item";
import axios from 'axios';

export const Women = () => {
  const [womenShoes, setShoes] = useState([]);

  useEffect(() => {
    fetchShoes();
  }, []);

  const fetchShoes = async () => {
    try {
      const response = await axios.get('http://localhost:5000/shoes/women');
      setShoes(response.data);
    } catch (error) {
      alert(error.response?.data?.error || "Flask server offline");
    }
  };

  return (
    <div className="men-shoe">
      <h2>Women's collection</h2>
      <div className="men-catalog">
        {womenShoes.map((shoe) => (
          <Link to={`/women/${shoe.Url}`} key={shoe.ItemID}>
            <Item id={shoe.ItemID} name={shoe.ItemName} image={shoe.Image} price={shoe.Price} gender={shoe.Gender}/>
          </Link>
        ))}
      </div>
    </div>
  );
};