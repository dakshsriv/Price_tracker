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
  return (
    <div>
      Link: <input name="lnk" value={link} onChange={(e) => setLink(e.target.value)}/>
      <br/>
      Email: <input name="eml" value={email} onChange={(e) => setEmail(e.target.value)}/>
      <button onClick={
        () => axios.post("http://127.0.0.1:8000/", {link2: link, email: email})
      }>Subscribe</button>
    </div>
  )
}

export default App;
