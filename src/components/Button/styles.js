import styled, { css } from "styled-components";

export const Container = styled.button`
  padding: 5px 10px;
  font-size: 0.6rem;
  width: 100px;
  background-color: var(--black);
  background-color: ${(props) => props.isVariantBlack && css`black`};
  background-color: ${(props) => props.isVariantRed && css`red`};
  border: none;
  border-radius: 20px;

  color: var(--white);
  color: ${(props) => props.isVariantBlack && css`white`};
  color: ${(props) => props.isVariantRed && css`white`};
  @media only screen and (min-width: 500px) {
    padding: 10px 20px;
    font-size: 0.7rem;
  }
  :hover {
    opacity: 0.7;
  }
  cursor: pointer;
`;
