import { useEffect, useState } from "react";
import { getProducts } from "../../utils/api.products.methods";
import { useNavigate } from "react-router-dom";
import { Container, List } from "./style";
import Button from "../../components/Button";

const ProductsPage = () => {
  const navigate = useNavigate();
  const handleClick = (id) => {
    navigate(`/products/${id}`);
  };
  const [products, setProducts] = useState([]);
  useEffect(() => {
    getProducts(setProducts);
  }, []);
  return (
    <>
      <Container>
        <header>
          <h1>Products</h1>
          <Button
            variantRed
            type={"button"}
            onClick={() => navigate("/cart")}
            children={"Ir para o carrinho"}
          ></Button>
        </header>
        <section>
          <List>
            {products.map((item) => (
              <li key={item.id} onClick={() => handleClick(item.id)}>
                <div>{item.name}</div>
                <div>Price: {item.price / 100}$</div>
              </li>
            ))}
          </List>
        </section>
      </Container>
    </>
  );
};

export default ProductsPage;
