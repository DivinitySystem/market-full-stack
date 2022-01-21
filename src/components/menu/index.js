import { AiOutlineArrowLeft } from "react-icons/ai";
import { useNavigate } from "react-router-dom";
const Menu = ({ route }) => {
  const navigate = useNavigate();
  return (
    <header>
      <AiOutlineArrowLeft size={30} onClick={() => navigate(route)} />
    </header>
  );
};

export default Menu;
