import React from 'react';
import { useNavigate } from 'react-router-dom';
import './Admin.css';

export const Admin = () => {
  const navigate = useNavigate();

  const handleNavigate = (path) => {
    navigate(path);
  };

  return (
    <div className="seller-dashboard">
      <h1>Welcome to the Admin Dashboard</h1>
      <div className="dashboard-buttons">
        <button className="dashboard-button" onClick={() => handleNavigate('/admin_view')}>
          View user accounts
        </button>
        <button className="dashboard-button" onClick={() => handleNavigate('/admin_add')}>
          Add New Item
        </button>
        <button className="dashboard-button" onClick={() => handleNavigate('/admin_remove')}>
          Remove Item
        </button>
        <button className="dashboard-button" onClick={() => handleNavigate('/update_form')}>
            Update Account
        </button>
        <button className="dashboard-button" onClick={() => handleNavigate('/update_quantity')}>
           Edit Item Quantity
        </button>
      </div>
    </div>
  );
};
