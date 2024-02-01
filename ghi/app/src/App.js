import { BrowserRouter, Routes, Route } from 'react-router-dom';
import MainPage from './MainPage';
import Nav from './Nav';
import HatList from "./HatList";
import HatForm from "./HatForm";
import ShoeList from "./ShoeList";
import ShoeForm from "./ShoeForm";

function App() {

  return (
    <BrowserRouter>
      <Nav />
      <div className="container">
        <Routes>
          <Route path="/" element={<MainPage />} />
          <Route path="/hats" element={<HatList /> } />
          <Route path="/hats/new" element={<HatForm /> } />
          <Route path="/shoes" element={<ShoeList /> } />
          <Route path="/shoes/new" element={<ShoeForm /> } />
        </Routes>
      </div>
    </BrowserRouter>
  );
}

export default App;
