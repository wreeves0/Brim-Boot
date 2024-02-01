import { BrowserRouter, Routes, Route } from 'react-router-dom';
import MainPage from './MainPage';
import Nav from './Nav';
import HatList from "./HatList";
import HatForm from "./HatForm";
import ShoesList from './ShoesList';

function App() {
  // if (props.hats === undefined) {
  //   return null;
  // }

  return (
    <BrowserRouter>
      <Nav />
      <div className="container">
        <Routes>
          <Route path="/" element={<MainPage />} />
        </Routes>
      </div>
    </BrowserRouter>
  );
}

export default App;
