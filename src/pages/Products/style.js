import styled from "styled-components";

export const Container = styled.main`
  display: flex;
  flex-direction: column;
  align-items: center;
  h1 {
    margin: 20px;
  }
  header {
    display: flex;
    flex-direction: row;
    justify-content: space-around;
    align-items: center;
    button {
      margin-left: 20%;
      width: 200px;
    }
  }
`;

export const List = styled.ul`
  display: flex;
  flex-direction: column;
  @media only screen and (min-width: 600px) {
    flex-direction: row;
  }
  justify-content: space-between;
  li {
    margin: 20px;
    border: 1px solid black;
    list-style: none;
    padding: 20px;
    background-color: #add8e6;
    border-radius: 20px;
    cursor: pointer;
    :hover {
      opacity: 0.7;
    }
  }
`;
