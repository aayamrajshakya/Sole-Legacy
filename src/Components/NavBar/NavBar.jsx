import "./NavBar.css";
import { BrowserRouter as Router, Route, Link } from "react-router-dom";

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
        <div className="nav-login-cart">
            <button>Login</button>
        </div>
    </div>
  )
}
