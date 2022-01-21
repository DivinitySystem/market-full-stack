import Form from "../../components/Form";
import Input from "../../components/Input";
import { Link } from "react-router-dom";
import { useState } from "react";
import { register } from "../../utils/api.user.methods";
import { useNavigate } from "react-router-dom";
import Button from "../../components/Button";
import { Container } from "./style";
import Menu from "../../components/menu";
const Register = () => {
  const navigate = useNavigate();
  const [nick_name, setnick_name] = useState("");
  const [password, setPassword] = useState("");
  const [email, setEmail] = useState("");
  const [error, setError] = useState("");

  const handleClick = () => {
    register({ nick_name, email, password, navigate, setError });
  };

  return (
    <>
      <Menu route={"/"} />
      <Container>
        <Form
          title="Register"
          children={
            <>
              <Input
                type={"text"}
                placeholder={"name"}
                onChange={(e) => setnick_name(e.target.value)}
              ></Input>
              <Input
                type={"password"}
                placeholder={"password"}
                onChange={(e) => setPassword(e.target.value)}
              ></Input>
              <Input
                type={"text"}
                placeholder={"email"}
                onChange={(e) => setEmail(e.target.value)}
              ></Input>
            </>
          }
        />
        <Button onClick={handleClick} type={"button"} variantBlack>
          Sign Up
        </Button>
        <p>
          Already have an account? <Link to="/login">Log In</Link>
        </p>
        {error && <span>{error}</span>}
      </Container>
    </>
  );
};

export default Register;
