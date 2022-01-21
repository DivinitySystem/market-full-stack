import jwtDecode from "jwt-decode";
import api from "../services/api";

export const register = ({
  nick_name,
  email,
  password,
  navigate,
  setError,
}) => {
  api
    .post("user", {
      nick_name: nick_name,
      email: email,
      password: password,
    })
    .then((res) => {
      navigate("/login");
    })
    .catch((e) => {
      setError(e.response.data.error);
    });
};

export const login = ({ email, password, setError, navigate }) => {
  api
    .post("login", {
      email: email,
      password: password,
    })
    .then((res) => {
      localStorage.setItem("foodToken", res.data.token);
      navigate("/products");
    })
    .catch((e) => setError(e.response.data.error));
};

export const patchUser = ({ nick_name }) => {
  const id = jwtDecode(localStorage.getItem("foodToken")).sub.id;
  api.patch(
    `user/${id}`,
    {
      nick_name: nick_name,
    },
    {
      headers: {
        Authorization: `Bearer ${localStorage.getItem("foodToken")}`,
      },
    }
  );
};

export const deleteUser = () => {
  const token = localStorage.getItem("foodToken");
  const id = jwtDecode(token).sub.id;
  api.delete(`user/${id}`, {
    headers: { Authorization: `Bearer ${token}` },
  });
};
