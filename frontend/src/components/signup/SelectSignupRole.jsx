import React from 'react';
import { Link } from 'react-router-dom';
import './signup.css';

const SelectSignupRole = () => {
  return (
    <div className="container">
      <div className="signup-box">
        <Link to="/Signup_customer" className="signup-button">Signup as Customer</Link>
        <Link to="/Signup_artisan" className="signup-button">Signup as Artisan</Link>
      </div>
    </div>
  );
};

export default SelectSignupRole;
