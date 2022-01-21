import styled from "styled-components";

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
    align-items: center;
    justify-content: center;
    button {
      width: 150px;
      margin: 4%;
    }
  }
`;

export const Container = styled.main`
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  section {
    list-style: none;
    background-color: wheat;
    width: 300px;
    display: flex;
    align-items: center;
    justify-content: center;
    flex-direction: column;
    border-radius: 20px;
    height: 200px;
    li {
      margin: 10px;
    }
  }
`;
