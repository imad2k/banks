import React, {useState, useEffect} from 'react'; 
import '../App.css';


export default function NewBank() {
    
    const [inputAddress, setAddress] = useState('');
    const [inputCity, setCity] = useState('');
    const [inputState, setusState] = useState('');
    const [inputBranchID, setBranchID] = useState('');
    



        function addBranch2() {
            
            const data = {
                address: inputAddress,
                city: inputCity,
                state: inputState,
                branch_id: inputBranchID
              };

              console.log(data);
            const configs = {
              method: "POST",
              headers: {"Content-Type":"application/json"},
              mode: "no-cors",
              body: JSON.stringify(data)
            }
            fetch("http://127.0.0.1:5000/api/v1/add_branch", configs)
          }
    
    
    return (
        <div>
            
                <div className='inputFeildWrapper'>
                    <div><h1 className='bankWrapperheader'>Add a New Branch</h1></div>
                    <input 
                        type='text'
                        placeholder='Branch ID'
                        onChange={e => setBranchID(e.target.value)}
                        className='inputFields'
                    />
                    <br />
                    <input 
                        type='text'
                        placeholder='Address'
                        onChange={e => setAddress(e.target.value)}
                        className='inputFields'
                    />
                    <br />

                    <input 
                        type='text'
                        placeholder='City'
                        onChange={e => setCity(e.target.value)}
                        className='inputFields'
                    />
                    <br />

                    <input 
                        type='text'
                        placeholder='State'
                        onChange={e => setusState(e.target.value)}
                        className='inputFields'
                    />
                    <br />
                </div>

                <div>
                    <button className='submit_button' onClick={e => addBranch2()}>Add</button>
                </div>
                
        </div>
    )
}
