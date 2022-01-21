import { Container } from "./styles";

export const Button = ({
  type,
  onClick,
  variantBlack,
  variantRed,
  children,
}) => {
  return (
    <Container
      type={type}
      onClick={onClick}
      isVariantBlack={variantBlack}
      isVariantRed={variantRed}
    >
      {children}
    </Container>
  );
};

export default Button;
