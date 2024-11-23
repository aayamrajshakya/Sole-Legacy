import React from 'react';
import { useNavigate } from 'react-router-dom';
import './Seller.css';

const Seller = () => {
  const navigate = useNavigate();

  const handleNavigate = (path) => {
    navigate(path);
  };

  return (
    <div className="seller-dashboard">
      <h1>Welcome to Your Seller Dashboard</h1>
      <div className="dashboard-buttons">
        <button className="dashboard-button" onClick={() => handleNavigate('/seller-add-product')}>
          Add New Product
        </button>
        <button className="dashboard-button" onClick={() => handleNavigate('/seller-listings')}>
          View Listings
        </button>
      </div>
    </div>
  );
};

export default Seller;
