import './index.css';

import React, { useEffect, useState } from "react";
import ReactDOM from "react-dom";
import ReactDataGrid from "react-data-grid";


const url = 'http://localhost:8000/drones/'

async function getDronesData(){

  let response = await fetch(url);

  let drones = await response.json();

  return drones.map(drone =>{
    return {
      id: drone.id,
      name: drone.name,
      brand: drone.brand,
      camerabrand: drone.camera.brand,
      cameramodel: drone.camera.model,
      resolution: drone.camera.resolution,
      checkin: drone.check_in,
      serialnumber: drone.serial_number
    }
  });
}

async function addDrones(){
  let data = {
    name: document.getElementById("name").value,
    brand: document.getElementById("brand").value,
    serial_number: document.getElementById("serial").value,
    camera: {
      model: document.getElementById("cameramodel").value,
      resolution: document.getElementById("cameraresolution").value,
      brand: document.getElementById("camerabrand").value
    }
  }
  var myHeaders = new Headers();
  myHeaders.append("x-fakeauth-x", document.getElementById("writeaccess").checked ? 0:1 );
  myHeaders.append("Content-Type", "application/json");
  
  var raw = JSON.stringify(data)

  var requestOptions = {
    method: 'POST',
    headers: myHeaders,
    body: raw,
    redirect: 'follow'
  };
  
  await fetch(url, requestOptions)
}

const defaultColumnProperties = {
  sortable: true,
  width: 120
};

const columns = [
  {
    key: "id",
    name: "ID",
    sortDescendingFirst: true
  },
  {
    key: "name",
    name: "Name"
  },
  {
    key: "brand",
    name: "Brand"
  },
  {
    key: "camerabrand",
    name: "Camera Brand"
  },
  {
    key: "cameramodel",
    name: "Camera Model"
  },
  {
    key: "resolution",
    name: "Resolution"
  },
  {
    key: "checkin",
    name: "Check In"
  },
  {
    key: "serialnumber",
    name: "Serial Number"
  }
].map(c => ({ ...c, ...defaultColumnProperties }));


const sortRows = (initialRows, sortColumn, sortDirection) => rows => {
  const comparer = (a, b) => {
    if (sortDirection === "ASC") {
      return a[sortColumn] > b[sortColumn] ? 1 : -1;
    } else if (sortDirection === "DESC") {
      return a[sortColumn] < b[sortColumn] ? 1 : -1;
    }
  };
  return sortDirection === "NONE" ? initialRows : [...rows].sort(comparer);
};

function Example() {
  const [rows, setRows] = useState([]);

  useEffect(async () => {
    let x = await getDronesData()
    setRows(x)
  }, []);

  const wrapper = async () => {
    await addDrones()
    let x = await getDronesData()
    setRows(x)
  }

  return (
    <div>
      <form id="form">
        <input id="name" placeholder="name" type="text"></input>
        <input id="brand" placeholder="brand" type="text"></input>
        <input id="camerabrand" placeholder="optical's brand" type="text"></input>
        <input id="cameramodel" placeholder="optical's model" type="text"></input>
        <input id="cameraresolution" placeholder="resolution" type="text"></input>
        <input id="serial" placeholder="serial" type="text"></input>
        <label>Write access: </label>
        <input id="writeaccess" type="checkbox"></input>
        <button onClick={(e) => {e.preventDefault(); wrapper()} }>Save</button>
      </form>
      <ReactDataGrid
        columns={columns}
        rowGetter={i => rows[i]}
        rowsCount={rows.length}
        minHeight={500}
        onGridSort={(sortColumn, sortDirection) =>
          setRows(sortRows(rows, sortColumn, sortDirection))
        }
      />
    </div>
  );
}

const rootElement = document.getElementById("root");
ReactDOM.render(<Example />, rootElement);
