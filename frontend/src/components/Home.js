import React, {useState, useEffect} from 'react';
import Bank from './Bank'; 

function Home() {
  
    const [branchData, setBranchData] = useState([]);
    
    useEffect(() => {
      const asyncCall = async () => {
        try{
          const response = await fetch('http://127.0.0.1:5000/api/v1/branches');
          const output = await response.json();
          setBranchData(output)        
        } catch (error) {
          console.log(error)
        }
      }
  
      asyncCall();
    }, []);
  
    
    
    return (
        <div>
            <div className='banksWrapper'>
                <Bank data={branchData}/>
            </div>
            
        </div>
    );
    }

    
    export default Home;