import api from "../services/api";

export const getProducts = (setProducts) => {
  api.get("products").then((res) => {
    setProducts(res.data);
  });
};
export const getProductById = ({ id, setProduct, setError }) => {
  api
    .get(`products/${id}`)
    .then((res) => setProduct(res.data))
    .catch((e) => setError(e.response.data.error));
};

export const getBill = (data, setBill) => {
  api.post("products", data).then((res) => setBill(res.data));
};
