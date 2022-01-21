import { useContext, useEffect, useState } from "react";
import { getProductById } from "../../utils/api.products.methods";
import { useParams } from "react-router-dom";
import { Container, List, Error } from "./style";
import Button from "../../components/Button";
import { CartContext } from "../../providers/cart";
import Menu from "../../components/menu";

const IndividualProduct = () => {
  const id = useParams().id;
  const { addToCart } = useContext(CartContext);
  const [product, setProduct] = useState({});
  const [error, setError] = useState("");

  useEffect(() => {
    getProductById({ id, setProduct, setError });
  }, [id]);
  return !product.name ? (
    <>
      <Menu route={"/products"} />

      <Error>
        {" "}
        <span>{error}</span>
      </Error>
    </>
  ) : (
    <>
      <Menu route={"/products"} />
      <>
        <Container>
          <header>
            <h1>{product.name}</h1>
          </header>
          <Container>
            <div>Normal price: {product.price / 100}$</div>
            <List>
              {product.promotions.map((item) => (
                <li>
                  <div>Promotion: {item.type}</div>
                  {item?.free_qty && <div>Free quantity: {item.free_qty}</div>}
                  {item?.required_qty && (
                    <div>Required quantity: {item.required_qty}</div>
                  )}
                  {item?.amount && <div>Amount: {item.amount}</div>}
                  {item?.price && <div>New Price: {item.price / 100}$</div>}
                </li>
              ))}
            </List>
          </Container>
          <Button
            children={"Adicionar no carrinho"}
            onClick={() => addToCart(product)}
            variantBlack
            type={"button"}
          ></Button>
        </Container>
      </>
    </>
  );
};

export default IndividualProduct;
