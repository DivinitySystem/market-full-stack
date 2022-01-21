import Button from "../Button";
import { useContext, useEffect, useState } from "react";
import { CartContext } from "../../providers/cart";

const ItemCart = ({ item, setDetectChange, detectChange }) => {
  const { removeFromCart } = useContext(CartContext);
  const [quantity, setQuantity] = useState(item.quantity);
  const [random, setRandom] = useState(0);

  useEffect(() => {
    setQuantity(item.quantity);
  }, [random, quantity, item.quantity]);

  return (
    <>
      <li>
        <div>{item.name}</div>
        <div>Individual Price {item.price / 100}$</div>
        <div>Quantity on cart: {quantity}</div>
        <div>Total product price = {(item.price * quantity) / 100}/$</div>
        <Button
          onClick={() => {
            setRandom(random + 1);
            removeFromCart(item.id);
            setDetectChange(detectChange + 1);
          }}
          children={"Remove 1 from cart"}
          variantBlack
        />
      </li>
    </>
  );
};

export default ItemCart;
