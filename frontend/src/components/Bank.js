import React from 'react';
import '../App.css'


export default function Bank({ data }) {
    
    

    return (
        <>
            {data.map((bank,index) => (
                <div key={index} className='bankCard'>
                    
                    <div>
                        <p className='title'>Branch ID</p>
                        <p className='results'>{bank.branch_id}</p>
                    </div>
                    
                    <div>
                        <p className='title'>Address</p>
                        <p className='results'>{bank.address}</p>
                    </div>
                    
                    <div>
                        <p className='title'>City</p>
                        <p className='results'>{bank.city}</p>
                    </div>
                    
                    <div>
                        <p className='title'>State</p>
                        <p className='results'>{bank.state}</p>
                    </div>
                </div>
            ))}
        </>
    )
}
