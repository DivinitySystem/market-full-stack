const Input = ({ type, onChange, placeholder, error }) => {
  return (
    <>
      <input type={type} onChange={onChange} placeholder={placeholder}></input>
      {error && <span>{error}</span>}
    </>
  );
};

export default Input;
