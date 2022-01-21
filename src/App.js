import AppRoutes from "./routes";
import { CartProvider } from "./providers/cart";
function App() {
  return (
    <>
      <CartProvider>
        <AppRoutes />
      </CartProvider>
    </>
  );
}

export default App;
