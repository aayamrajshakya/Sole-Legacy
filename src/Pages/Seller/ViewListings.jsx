import React, { useState } from 'react';
import './ViewListings.css';

const ViewListings = () => {
    const [searchItemName, setSearchItemName] = useState('');
    const [listings, setListings] = useState([]);
    const [message, setMessage] = useState('');
    const [error, setError] = useState('');
    const [loading, setLoading] = useState(false);
    const [updateQuantity, setUpdateQuantity] = useState({});
    const [updating, setUpdating] = useState({});

    const handleSearch = async (e) => {
        e.preventDefault();
        setLoading(true);
        setMessage('');
        setError('');

        try {
            const response = await fetch(`http://localhost:5000/seller/listings?itemName=${encodeURIComponent(searchItemName)}`, {
                method: 'GET',
                credentials: 'include',
            });

            const data = await response.json();

            if (response.ok) {
                setListings(data.listings);
                setMessage(data.message);
            } else {
                setError(data.error);
                setListings([]);
            }
        } catch (err) {
            setError('Failed to connect to server');
            setListings([]);
        } finally {
            setLoading(false);
        }
    };

    const handleUpdateStock = async (itemId, quantity, addOrRemove) => {
        setUpdating(prev => ({ ...prev, [itemId]: true }));
        try {
            const response = await fetch('http://localhost:5000/seller/update-stock', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                credentials: 'include',
                body: JSON.stringify({
                    ItemID: itemId,
                    Quantity: parseInt(quantity),
                    AddOrRemove: addOrRemove
                })
            });

            const data = await response.json();

            if (response.ok) {
                // Update the local state with the new quantity
                setListings(listings.map(item => {
                    if (item.ItemID === itemId) {
                        return {
                            ...item,
                            Quantity: addOrRemove ? 
                                item.Quantity + parseInt(quantity) : 
                                item.Quantity - parseInt(quantity)
                        };
                    }
                    return item;
                }));
                setMessage(data.message);
                setUpdateQuantity(prev => ({ ...prev, [itemId]: '' }));
            } else {
                setError(data.error);
            }
        } catch (err) {
            setError('Failed to update stock');
        } finally {
            setUpdating(prev => ({ ...prev, [itemId]: false }));
        }
    };

    const handleRemoveProduct = async (itemId) => {
        if (!window.confirm('Are you sure you want to remove this product?')) {
            return;
        }

        setUpdating(prev => ({ ...prev, [itemId]: true }));
        try {
            const response = await fetch('http://localhost:5000/seller/remove-product', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                credentials: 'include',
                body: JSON.stringify({
                    ItemID: itemId
                })
            });

            const data = await response.json();

            if (response.ok) {
                setListings(listings.filter(item => item.ItemID !== itemId));
                setMessage(data.message);
            } else {
                setError(data.error);
            }
        } catch (err) {
            setError('Failed to remove product');
        } finally {
            setUpdating(prev => ({ ...prev, [itemId]: false }));
        }
    };

    const formatPrice = (price) => {
        return typeof price === 'number' 
            ? `$${price.toFixed(2)}` 
            : price;
    };

    return (
        <div className="view-listings-container">
            <div className="search-section">
                <h2>View Product Listings</h2>
                <form onSubmit={handleSearch} className="search-form">
                    <div className="search-input-group">
                        <input
                            type="text"
                            value={searchItemName}
                            onChange={(e) => setSearchItemName(e.target.value)}
                            placeholder="Enter item name..."
                            required
                        />
                        <button type="submit" disabled={loading || !searchItemName.trim()}>
                            {loading ? 'Searching...' : 'Search'}
                        </button>
                    </div>
                </form>
            </div>

            {error && <div className="error-message">{error}</div>}
            {message && <div className="info-message">{message}</div>}



            {listings.length > 0 && (
                <div className="listings-grid">
                    {listings.map((item) => (
                        <div key={item.ItemID} className="listing-card">
                            <div className="listing-image">
                                <img src={`${process.env.PUBLIC_URL}/${item.Gender}/${item.Image}`} alt={item.ItemName} />
                            </div>
                            <div className="listing-details">
                                <h3>{item.ItemName}</h3>
                                <p className="description">{item.Description}</p>
                                <div className="listing-meta">
                                    <span className="price">{formatPrice(item.Price)}</span>
                                    <span className="quantity"> {item.Quantity}</span>
                                    <span className="gender">{item.Gender}</span>
                                </div>
                                <div className="stock-controls">
                                    <div className="quantity-update">
                                        <input
                                            type="number"
                                            min="1"
                                            value={updateQuantity[item.ItemID] || ''}
                                            onChange={(e) => setUpdateQuantity({
                                                ...updateQuantity,
                                                [item.ItemID]: e.target.value
                                            })}
                                            placeholder="Quantity"
                                        />
                                        <div className="quantity-buttons">
                                            <button
                                                onClick={() => handleUpdateStock(
                                                    item.ItemID,
                                                    updateQuantity[item.ItemID],
                                                    true
                                                )}
                                                disabled={!updateQuantity[item.ItemID] || updating[item.ItemID]}
                                            >
                                                Add Stock
                                            </button>
                                            <button
                                                onClick={() => handleUpdateStock(
                                                    item.ItemID,
                                                    updateQuantity[item.ItemID],
                                                    false
                                                )}
                                                disabled={!updateQuantity[item.ItemID] || updating[item.ItemID]}
                                            >
                                                Remove Stock
                                            </button>
                                        </div>
                                    </div>
                                    <button
                                        className="remove-button"
                                        onClick={() => handleRemoveProduct(item.ItemID)}
                                        disabled={updating[item.ItemID]}
                                    >
                                        {updating[item.ItemID] ? 'Removing...' : 'Remove Product'}
                                    </button>
                                </div>
                            </div>
                        </div>
                    ))}
                </div>
            )}

            {loading && (
                <div className="loading-spinner">
                    <div className="spinner"></div>
                    <p>Loading listings...</p>
                </div>
            )}
        </div>
    );
};

export default ViewListings;