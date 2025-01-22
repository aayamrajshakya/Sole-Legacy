import React, { useState, useEffect } from 'react';
import './HomepageShowcase.css';
import { Link } from "react-router-dom";
import { Item } from "../Item/Item";
import axios from 'axios';

export const HomepageShowcase = () => {
  const [showcaseShoes, setShowcaseShoes] = useState([]);

  useEffect(() => {
    fetchShowcaseShoes();
  }, []);

  const fetchShowcaseShoes = async () => {
    try {
      const response = await axios.get('http://localhost:5000/shoes/showcase');
      setShowcaseShoes(response.data);
    } catch (error) {
      alert(error.response?.data?.error || "Flask server offline");
    }
  };

  return (
    <div className="eachShoe">
      <h2>Our best sellers</h2>
      <div className="shoe-showcase">
        {showcaseShoes.map((shoe) => (
          <Link to={`/men/${shoe.Url}`} key={shoe.ItemID}>
            <Item id={shoe.ItemID} name={shoe.ItemName} image={shoe.Image} price={shoe.Price} gender={shoe.Gender} />
          </Link>
        ))}
      </div>
    </div>
  );
};