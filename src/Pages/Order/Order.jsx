import React, { useState, useEffect } from 'react';
import './Order.css';

const Order = () => {
  const [orders, setOrders] = useState([]);
  const [selectedOrder, setSelectedOrder] = useState(null);
  const [error, setError] = useState('');

  useEffect(() => {
    fetchOrders();
  }, []);

  const fetchOrders = async () => {
    try {
      const response = await fetch('http://localhost:5000/orders', {
        credentials: 'include',
      });
      const data = await response.json();
      
      if (response.ok) {
        setOrders(data.orders);
      } else {
        setError(data.error);
      }
    } catch (err) {
      setError('Failed to fetch orders');
    }
  };

  const fetchOrderDetails = async (orderId) => {
    try {
      const response = await fetch(`http://localhost:5000/order/${orderId}`, {
        credentials: 'include',
      });
      const data = await response.json();
      
      if (response.ok) {
        setSelectedOrder(data);
      } else {
        setError(data.error);
      }
    } catch (err) {
      setError('Failed to fetch order details');
    }
  };

  return (
    <div className="orders-container">
      <h2 className="orders-title">Your Orders</h2>
      
      {error && <div className="error-message">{error}</div>}
      
      <div className="orders-grid">
        {orders.map((order) => (
          <div key={order.orderID} className="order-card">
            <div className="order-header">
              <h3>Order #{order.orderID}</h3>
              <span className="order-date">
                {new Date(order.orderDate).toLocaleDateString()}
              </span>
            </div>
            
            <div className="order-info">
              <p>Total Amount: ${order.totalAmount.toFixed(2)}</p>
            </div>
            
            <button 
              className="view-details-button"
              onClick={() => fetchOrderDetails(order.orderID)}
            >
              View Details
            </button>
            
            {selectedOrder && selectedOrder.orderID === order.orderID && (
              <div className="order-details">
                <h4>Order Items:</h4>
                <ul className="items-list">
                  {selectedOrder.items.map((item, index) => (
                    <li key={index}>
                      {item.itemName} x {item.quantity}
                    </li>
                  ))}
                </ul>
              </div>
            )}
          </div>
        ))}
      </div>
    </div>
  );
};

export default Order;