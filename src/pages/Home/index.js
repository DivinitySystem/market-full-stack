import logo from "../../assets/logo.png";
import Button from "../../components/Button";
import { Footer, Main, PageHeader } from "./styles";
import { useNavigate } from "react-router-dom";
const Home = () => {
  const navigate = useNavigate();
  const sendTo = (route) => {
    navigate(route);
  };
  return (
    <>
      <PageHeader>
        <img src={logo} alt="404"></img>
        <div>
          <Button
            children={"Sign Up"}
            variantBlack
            onClick={() => sendTo("/register")}
          ></Button>
          <Button
            children={"Sign In"}
            variantBlack
            onClick={() => sendTo("/login")}
          ></Button>
        </div>
      </PageHeader>
      <Main>
        <section>
          <p>
            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer sed
            odio pretium, tincidunt urna non, euismod lacus. Maecenas maximus
            sollicitudin rutrum. Sed eu semper orci. Mauris mauris libero,
            convallis eu quam eu, tempus vulputate nibh. Quisque sit amet magna
            eu tortor vestibulum congue in et neque. Suspendisse turpis justo,
            ornare ac lacinia eget, sodales ut justo. Donec ut elementum est. Ut
            et efficitur ex.
          </p>
          <p>
            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer sed
            odio pretium, tincidunt urna non, euismod lacus. Maecenas maximus
            sollicitudin rutrum. Sed eu semper orci. Mauris mauris libero,
            convallis eu quam eu, tempus vulputate nibh. Quisque sit amet magna
            eu tortor vestibulum congue in et neque. Suspendisse turpis justo,
            ornare ac lacinia eget, sodales ut justo. Donec ut elementum est. Ut
            et efficitur ex.
          </p>
        </section>
      </Main>
      <Footer>
        <span>Made by Priccila</span>
      </Footer>
    </>
  );
};

export default Home;
