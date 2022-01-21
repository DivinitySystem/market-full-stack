import { Container } from "./styles";

const Form = ({ title, children }) => {
  return (
    <Container>
      {title && <h1>{title}</h1>}
      {children}
    </Container>
  );
};

export default Form;
