import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import './Checkout.css';

const Checkout = () => {
  const [paymentMethod, setPaymentMethod] = useState('');
  const [error, setError] = useState('');
  const navigate = useNavigate();

  const handleCheckout = async () => {
    try {
      const response = await fetch('http://localhost:5000/order/checkout', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        credentials: 'include',
        body: JSON.stringify({ paymentMethod }),
      });

      const data = await response.json();

      if (response.ok) {
        alert(`Order placed successfully! Order ID: ${data.orderID}`);
        navigate('/orders');
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
      
      <div className="payment-section">
        <h3>Select Payment Method</h3>
        <div className="payment-options">
          {['Credit Card', 'PayPal', 'Debit Card', 'Apple Pay', 'Google Pay'].map((method) => (
            <button
              key={method}
              className={`payment-button ${paymentMethod === method ? 'selected' : ''}`}
              onClick={() => setPaymentMethod(method)}
            >
              {method}
            </button>
          ))}
        </div>
      </div>

      <button 
        className="checkout-button"
        onClick={handleCheckout}
        disabled={!paymentMethod}
      >
        Complete Purchase
      </button>
    </div>
  );
};

export default Checkout;