from requests import post, get

def test_get_food():
    url = "http://127.0.0.1:5000/products"

    food_data = get(url)

    food = food_data.json()[0]

    assert food_data.status_code == 200
    assert len(food_data.json()) == 4
    assert type(food_data.json()) == list
    assert 'name' in food
    assert 'price' in food
    assert 'id' in food


def test_get_the_bill():
    url = 'http://127.0.0.1:5000/products'
    burguer = [{ 
        "id": "PWWe3w1SDU",
        "name": "Amazing Burger!",
        "price": 999,
	    "quantity": 11,
        "promotions": [{
      "id": "ZRAwbsO2qM",
      "type": "BUY_X_GET_Y_FREE",
      "required_qty": 4,
      "free_qty": 3 }]}]

    response = post(url, json=burguer)

    assert response.status_code == 200
    assert 'total price' in response.json()
    assert 'total spent' in response.json()
    assert 'total disccount' in response.json()
    assert response.json()['total price'] == 10989
    assert response.json()['total spent'] == 4995
    assert response.json()['total disccount'] == 5994

    salad = [{
    "id": "C8GDyLrHJb",
    "quantity": 2,
    "name": "Amazing Salad!",
    "price": 499,
    "promotions": [
    {
      "id": "Gm1piPn7Fg",
      "type": "FLAT_PERCENT",
      "amount": 10
    }]}]

    response = post(url, json=salad)
    assert response.status_code == 200
    assert response.json()['total price'] == 2*499
    assert response.json()['total disccount'] == (2*499)/10
    assert response.json()['total spent'] == (2*499) - (2*499)/10 

    pizza = [{ "id": "Dwt5F7KAhi",
  "name": "Amazing Pizza!",
  "quantity": 3,
  "price": 1099,
  "promotions": [
    {
      "id": "ibt3EEYczW",
      "type": "QTY_BASED_PRICE_OVERRIDE",
      "required_qty": 2,
      "price": 1799
    }
  ]}]
    response = post(url, json=pizza)
    
    assert response.status_code == 200
    assert response.json()['total price'] == 3297
    assert response.json()['total disccount'] == 1799
    assert response.json()['total spent'] == 1498

    fries = [{ "id": "4MB7UfpTQs",
      "name": "Boring Fries!",
      "price": 199,
    	"quantity": 10,
      "promotions": [] }]

    response = post(url, json=fries)

    assert response.status_code == 200
    assert response.json()["total price"] ==  1990
    assert response.json()["total disccount"] ==  0
    assert response.json()["total spent"] == 1990

def test_get_all_products_bill():
    url = "http://127.0.0.1:5000/products"
    products = [
	{
  "id": "4MB7UfpTQs",
  "name": "Boring Fries!",
  "price": 199,
	"quantity": 1,
  "promotions": []
},
	{
  "id": "Dwt5F7KAhi",
  "name": "Amazing Pizza!",
	"quantity": 3,
  "price": 1099,
  "promotions": [
    {
      "id": "ibt3EEYczW",
      "type": "QTY_BASED_PRICE_OVERRIDE",
      "required_qty": 2,
      "price": 1799
    }
  ]
},
	
	{
  "id": "PWWe3w1SDU",
  "name": "Amazing Burger!",
  "price": 999,
	"quantity": 2,
  "promotions": [
    {
      "id": "ZRAwbsO2qM",
      "type": "BUY_X_GET_Y_FREE",
      "required_qty": 2,
      "free_qty": 1
    }
  ]
},
	{
  "id": "C8GDyLrHJb",
	"quantity": 1,
  "name": "Amazing Salad!",
  "price": 499,
  "promotions": [
    {
      "id": "Gm1piPn7Fg",
      "type": "FLAT_PERCENT",
      "amount": 10
    }
  ]
}
]
    response = post(url, json=products)
    assert response.status_code == 200
    assert response.json()['total price'] == 5993   
    assert response.json()['total disccount'] == 2847.9
    assert response.json()['total spent'] == 3145.1