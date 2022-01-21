import { createContext, useState } from "react";

export const CartContext = createContext([]);
export const CartProvider = ({ children }) => {
  const [cart, setCart] = useState([]);

  const addToCart = (item) => {
    if (cart.find((cartItem) => cartItem.id === item.id)) {
      const indexToUpdate = cart.findIndex(
        (itemOnCart) => itemOnCart.id === item.id
      );
      const newCart = cart;
      newCart[indexToUpdate].quantity += 1;
      setCart(newCart);
    } else {
      item.quantity = 1;
      setCart([...cart, item]);
    }
  };

  const removeFromCart = (id) => {
    const indexToRemove = cart.findIndex((itemOnCart) => itemOnCart.id === id);
    let newCart = cart;
    cart[indexToRemove].quantity - 1 === 0
      ? (newCart = cart.filter((item, idx) => idx !== indexToRemove))
      : (newCart[indexToRemove].quantity -= 1);
    setCart(newCart);
  };

  return (
    <CartContext.Provider
      value={{
        cart,
        removeFromCart,
        addToCart,
      }}
    >
      {children}
    </CartContext.Provider>
  );
};
