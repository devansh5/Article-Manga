import './App.css';
import {Route,Switch} from 'react-router-dom';
import Signup from './components/Signup/Signup';
import Login from './components/Login/Login';
import Root from './Root';
function App() {
  return (
    <Root>
      <Switch>
        <Route path="/signup" component={Signup} />
        <Route path="/login" component={Login} />
        {/* <Route path="/dashboard" component={Dasboard}/> */}
      </Switch>
    </Root>
  );
}

export default App;
