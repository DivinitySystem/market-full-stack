import styled from "styled-components";

export const PageHeader = styled.header`
  display: flex;
  align-items: center;
  justify-content: space-between;
  background-color: #41b6e6;
  img {
    width: 200px;
  }
  div {
    button {
      margin-left: 10px;
      margin-right: 30px;
    }
  }
`;

export const Main = styled.main`
  section {
    display: flex;
    justify-content: space-around;
    flex-direction: column;
    @media only screen and (min-width: 600px) {
      flex-direction: row;
    }
    p {
      display: flex;
      width: 300px;
      @media only screen and (min-width: 600px) {
        width: 400px;
      }
    }
  }
`;

export const Footer = styled.footer`
  display: flex;
  position: fixed;
  height: 50px;
  background-color: black;
  bottom: 0px;
  left: 0px;
  right: 0px;
  margin-bottom: 0px;
  align-items: center;
  justify-content: center;
  color: white;
`;
