import styled from "styled-components";

export const Container = styled.main`
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  h1 {
    margin: 20px;
  }
  button {
    width: 200px;
  }
`;

export const List = styled.ul`
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  li {
    margin: 20px;
    border: 1px solid black;
    list-style: none;
    padding: 20px;
    background-color: #add8e6;
    border-radius: 20px;
    font-size: 12px;
  }
`;

export const Error = styled.div`
  display: flex;
  align-items: center;
  justify-content: center;
  color: red;
  font-size: 50px;
`;
