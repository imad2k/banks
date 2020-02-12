import React, { useState } from 'react';
import '../App.css'


export default function Bank({ data }) {
    
    

    return (
        <>
            {data.map((bank,index) => (
                <div key={index} className='bankCard'>
                    <p>{bank.branch_id}</p>
                    <p>{bank.address}</p>
                    {/* <p></p> */}
                    <p><span>{bank.city}</span><span>{bank.state}</span></p>
                </div>
            ))}
        </>
    )
}
