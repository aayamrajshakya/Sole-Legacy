import React from 'react'
import './Item.css'

export const Item = ({ image, name, price, gender }) => {
  return (
    <div className="item">
      <div className="image">
      <img src={`${process.env.PUBLIC_URL}/${gender}/${image}`} />
      </div>
      <p className="item-name">{name}</p>
      <p className="item-price">${price}</p>
    </div>
  );
};