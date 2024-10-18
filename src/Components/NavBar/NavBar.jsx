import "./NavBar.css";
import { BrowserRouter as Router, Route, Link } from "react-router-dom";
import cart_icon from "../Assets/general/cart.png"
import login_icon from "../Assets/general/login.png"
import wishlist_icon from "../Assets/general/wishlist.png"

export const NavBar = () => {
  return (
    <div className='navbar'>
        <div className='nav-logo'>
            <h2>
            <Link to ="/">Sole Legacy</Link>
            </h2>
        </div>
        <ul className="nav-menu">
            <Link className="nav-link" to ="/women">Women</Link>
            <Link className="nav-link" to ="/men">Men</Link>
            <Link className="nav-link" to ="/">Home</Link>
        </ul>
        <div className="nav-icons">
          <Link to="/login" className="nav-login">
          <img src={login_icon} />
          </Link>
          <Link to="/cart" className="nav-cart">
          <img src={cart_icon} />
          </Link>
          <Link to="/wishlist" className="nav-wishlist">
          <img src={wishlist_icon} />
          </Link>
        </div>
    </div>
  )
}
