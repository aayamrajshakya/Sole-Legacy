import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import './Checkout.css';

const Checkout = () => {
  const [creditCardDetails, setCreditCardDetails] = useState({
    cardNumber: '',
    expiryDate: '',
    cvv: '',
  });
  const [error, setError] = useState('');
  const [success, setSuccess] = useState('');
  const navigate = useNavigate();

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setCreditCardDetails((prevDetails) => ({
      ...prevDetails,
      [name]: value,
    }));
  };

  const handleCheckout = async () => {
    const { cardNumber, expiryDate, cvv } = creditCardDetails;

    if (!cardNumber || !expiryDate || !cvv) {
      setError('Please fill out all fields');
      return;
    }

    try {
      const response = await fetch('http://localhost:5000/order/checkout', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        credentials: 'include',
        body: JSON.stringify({ 
          cardNumber, 
          expiryDate, 
          cvv
        }),
      });

      const data = await response.json();

      if (response.ok) {
        setSuccess(`Order placed successfully! Order ID: ${data.orderID}`);
        setTimeout(() => navigate('/orders'), 2000);
      } else {
        setError(data.error);
      }
    } catch (err) {
      setError('Failed to process checkout');
    }
  };

  return (
    <div className="checkout-container">
      <h2 className="checkout-title">Checkout</h2>
      
      {error && <div className="error-message">{error}</div>}
      {success && <div className="success-message">{success}</div>}

      <div className="credit-card-form">
        <label htmlFor="cardNumber">Card Number</label>
        <input
          type="text"
          id="cardNumber"
          name="cardNumber"
          value={creditCardDetails.cardNumber}
          onChange={handleInputChange}
          placeholder="Enter card number"
        />

        <label htmlFor="expiryDate">Expiry Date (MM/YY)</label>
        <input
          type="text"
          id="expiryDate"
          name="expiryDate"
          value={creditCardDetails.expiryDate}
          onChange={handleInputChange}
          placeholder="MM/YY"
        />

        <label htmlFor="cvv">CVV</label>
        <input
          type="text"
          id="cvv"
          name="cvv"
          value={creditCardDetails.cvv}
          onChange={handleInputChange}
          placeholder="Enter CVV"
        />

        <button
          className="checkout-button"
          onClick={handleCheckout}
        >
          Complete Purchase
        </button>
      </div>
    </div>
  );
};

export default Checkout;
