import React from 'react';
import { Link } from 'react-router-dom';


export default function NavBar() {
    return (
        <div className='navHeader'>
            <Link to='/home' className='navLink'>Home</Link>
            <Link to='/newbank' className='navLink'> Add New Bank</Link>
            <Link to='/newemployee' className='navLink'>Add New Employee</Link>
            
        </div>
    )
}
