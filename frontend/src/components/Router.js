import React from 'react';
import { Route } from 'react-router-dom';
import NewEmployee from './NewEmployee';
import NewBank from './NewBank';
import Home from './Home';

export default function Router() {
    return (
        <div>
            <Route exact path='/home' component={Home}/>
            <Route path='/newbank' component={NewBank}/>
            <Route path='/newemployee' component={NewEmployee}/>
            
        </div>
    )
}
