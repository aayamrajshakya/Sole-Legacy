import React, { useState, useEffect } from 'react';
import "./Men.css";
import { Link } from "react-router-dom";
import { Item } from "../Item/Item";
import axios from 'axios';

export const Men = () => {
  const [menShoes, setShoes] = useState([]);

  useEffect(() => {
    fetchShoes();
  }, []);

  const fetchShoes = async () => {
    try {
      const response = await axios.get('http://localhost:5000/shoes/men');
      setShoes(response.data);
    } catch (error) {
      alert(error.response?.data?.error || "Flask server offline");
    }
  };

  return (
    <div className="men-shoe">
      <h2>Men's collection</h2>
      <div className="men-catalog">
        {menShoes.map((shoe) => (
          <Link to={`/men/${shoe.Url}`} key={shoe.ItemID}>
            <Item id={shoe.ItemID} name={shoe.ItemName} image={shoe.Image} price={shoe.Price} gender={shoe.Gender}/>
          </Link>
        ))}
      </div>
    </div>
  );
};