import Menu from "../../components/menu";
import { useContext, useState } from "react";
import { CartContext } from "../../providers/cart";
import ItemCart from "../../components/ItemCart";
import { List, Container } from "./style";
import { getBill } from "../../utils/api.products.methods";
import { useEffect } from "react/cjs/react.development";

const Cart = () => {
  const { cart } = useContext(CartContext);
  const [bill, setBill] = useState({});
  const [detectChange, setDetectChange] = useState(0);
  useEffect(() => {
    getBill(cart, setBill);
  }, [cart, detectChange]);
  return (
    <>
      <Menu route={"/products"} />

      <Container>
        <List>
          {cart.map((item) => (
            <ItemCart
              setDetectChange={setDetectChange}
              key={item.id}
              item={item}
              detectChange={detectChange}
            />
          ))}
        </List>
        <section>
          <h2>Bill</h2>
          <li>Total price: {bill.total_price / 100}$</li>
          <li>Total disccount: {bill.total_disccount / 100}$</li>
          <li>Total to pay: {bill.total_spent / 100}$</li>
        </section>
      </Container>
    </>
  );
};

export default Cart;
