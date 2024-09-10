import React from "react";
import { Routes, Route } from "react-router-dom";
import LoginPanel from "./components/Login/Login";
import Dealers from './components/Dealers/Dealers';
import Register from './components/Register/Register'; // Import the registration component

function App() {
  return (
    <Routes>
      <Route path="/login" element={<LoginPanel />} />
      <Route path="/register" element={<Register />} />
      <Route path="/dealers" element={<Dealers />} /> {/* Add the Dealers route */}
    </Routes>
  );
}

export default App;
