import './App.css';
import { useState } from 'react';
import axios from 'axios';

function App() {
  return (
    <div className="App">
      <h1>Price tracker</h1>
      <GetStats/>
    </div>
  );
}

function GetStats() {
  const [link, setLink] = useState('')
  const [email, setEmail] = useState('')
  const [msg, setMsg] = useState('')
  return (
    <div>
      <label>Link: <input name="lnk" value={link} onChange={(e) => setLink(e.target.value)}/></label>
      Email: <input name="eml" value={email} onChange={(e) => setEmail(e.target.value)}/>
      <button onClick={
        () => axios.post("https://dev.dakshsrivastava.com/", {"link2": link, "email": email}).then(setMsg('Subscribed!'))
      }>Subscribe</button>
      <button onClick={
        () => axios.post("https://dev.dakshsrivastava.com/delete/", {"link2": link, "email": email}).then(setMsg('Unsubscribed!'))
      }>Unsubscribe</button>
      <p id="Verify">{msg}</p>
      
    </div>
  )
}

export default App;
