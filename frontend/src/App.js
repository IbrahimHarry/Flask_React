import logo from './logo.svg';
import './App.css';
import { useEffect , useState} from 'react';

function App() {

  const [data, setData] = useState([]);

  useEffect(()=>{
    fetch('http://127.0.0.1:5000/employess').then(async (data)=>{
      console.log(await data.json())
    })
  })
  useEffect(() => {
    fetch('http://127.0.0.1:5000/employess')
      .then((response) => response.json())
      .then((data) => setData(data));
  }, []);

  const onDelete = (item)=>{
    // alert(JSON.stringify(item))
    debugger;
    fetch(`http://127.0.0.1:5000/deleteEmp?empid=${item._id.$oid}`)
    // .then((response) => response.json())
    .then((data) => console.log(data));
  }

  return (
    <div className="App">
      <table>
      <thead>
        <tr>
          <th>Name</th>
          <th>Age</th>
          <th>Email</th>
          <th>Action</th>
        </tr>
      </thead>
      <tbody>
        {data.map((item) => (
          <tr key={item.name}>
             <td>{item.name}</td>
            <td>{item.age}</td>
            <td>{item.email}</td>
            <td><button onClick={()=> onDelete(item)}>Delete</button></td>
          </tr>
        ))}
      </tbody>
    </table>
    </div>
  );
}

export default App;
