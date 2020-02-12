import React, { useState, useEffect } from 'react';
import './App.css';
import Bank from './components/Bank';


function App() {
  
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


    
    console.log(branchData)

  
  
  
  
  
  return (
    <div className="App" >
      {/* <button onClick={e => getBranches()}>Get Branches</button> */}
      <div>
      <Bank data={branchData}/>
      
      
      </div>
    </div>
  );
}

export default App;
