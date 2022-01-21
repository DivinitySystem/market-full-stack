import styled from "styled-components";

export const Container = styled.main`
  display: flex;
  align-items: center;
  flex-direction: column;
  font-size: 1.2rem;

  input {
    padding: 5px;
    margin-bottom: 8px;
    border-radius: 10px;
  }

  button {
    margin: 10px;
    width: 150px;
  }
  span {
    font-size: 12px;
    color: red;
  }
`;
