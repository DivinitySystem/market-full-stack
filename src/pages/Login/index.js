import Form from "../../components/Form";
import Input from "../../components/Input";
import { Link } from "react-router-dom";
import { useState } from "react";
import { login } from "../../utils/api.user.methods";
import Button from "../../components/Button";
import { Container } from "./style";
import { useNavigate } from "react-router-dom";
import Menu from "../../components/menu";

const Login = () => {
  const [password, setPassword] = useState("");
  const [email, setEmail] = useState("");
  const [error, setError] = useState("");
  const navigate = useNavigate();
  const handleClick = (email, password) => {
    login({ email, password, setError, navigate });
  };

  return (
    <>
      <Menu route={"/"} />
      <Container>
        <Form
          title="Login"
          children={
            <>
              <Input
                type={"text"}
                placeholder={"email"}
                onChange={(e) => setEmail(e.target.value)}
              ></Input>
              <Input
                type={"password"}
                placeholder={"password"}
                onChange={(e) => setPassword(e.target.value)}
              ></Input>
            </>
          }
        />
        <Button
          onClick={() => handleClick(email, password)}
          type={"button"}
          variantBlack
        >
          Sign Up
        </Button>
        <p>
          Don't have a account yet? <Link to="/register">Sign Up</Link>
        </p>
        {error && <span>{error}</span>}
      </Container>
    </>
  );
};

export default Login;
