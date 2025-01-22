import React from 'react';
import './App.css';
import Footer from "./Components/Footer/Footer";
import { NavBar } from './Components/NavBar/NavBar';
import { Homepage } from './Pages/Homepage/Homepage';
import { Men } from './Pages/Men/Men';
import { Women } from './Pages/Women/Women';
import { Login } from './Pages/Authentication/Login';
import { Register } from './Pages/Register/Register';
import { Cart } from './Pages/Cart/Cart';
import { Wishlist } from './Pages/Wishlist/Wishlist';
import { IndivShoe } from './Pages/IndivShoe/IndivShoe';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import { Dashboard } from './Pages/Authentication/Dashboard';
import { Admin } from './Pages/Admin/Admin'
import { UserDirectory } from './Pages/Admin/UserDirectory';
import { AdminAdd } from "./Pages/Admin/AdminAdd";
import { RemoveItem } from "./Pages/Admin/RemoveItem";
import { UpdateQuantity } from "./Pages/Admin/UpdateQuantity";
import { UpdateAccount } from "./Pages/Admin/UpdateAccount";
import { PageNotFound } from './Components/PageNotFound/PageNotFound';
import { Search } from './Pages/Search/Search';
import SellerAddProduct from './Pages/Seller/SelllerAddProduct';
import ViewListings from './Pages/Seller/ViewListings';
import Order from './Pages/Order/Order';
import Checkout from './Pages/Order/Checkout';
import Seller from './Pages/Seller/Seller';

function App() {
  return (
    <div className="App">
      <BrowserRouter>
        <NavBar />
        <Routes>
          <Route path='/' element={<Homepage />} />
          <Route path='/women' element={<Women />} />
          <Route path='/women/:url' element={<IndivShoe />} />
          <Route path='/men' element={<Men />} />
          <Route path='/men/:url' element={<IndivShoe />} />
          <Route path='/login' element={<Login />} />
          <Route path='/register' element={<Register />} />
          <Route path='/cart' element={<Cart />} />
          <Route path='/wishlist' element={<Wishlist />} />
          <Route path='/dashboard' element={<Dashboard />} />
          <Route path='/admin' element={<Admin />} />
          <Route path='/admin_view' element={<UserDirectory />} />
          <Route path='/admin_add' element={<AdminAdd />} />
          <Route path='/admin_remove' element={<RemoveItem />} />
          <Route path='/update_quantity' element={<UpdateQuantity />} />
          <Route path='/update_form' element={<UpdateAccount />} />
          <Route path='/seller' element={<Seller />} />
          <Route path='/seller-add-product' element={<SellerAddProduct />} />
          <Route path='/seller-listings' element={<ViewListings />} />
          <Route path="/checkout" element={<Checkout />} />
          <Route path="/orders" element={<Order />} />
          <Route path='/search' element={<Search />} />
          <Route path="*" element={<PageNotFound />} />
        </Routes>
      </BrowserRouter>
      <Footer />
    </div>
  );
}

export default App;
