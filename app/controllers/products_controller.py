from flask import jsonify, request
import json
from math import floor


def get_all_products():
   
    with open('app/assets/products.json') as json_file:
      products = json.load(json_file)['response']['jsonBody']

    return jsonify(products)

def get_product_by_id(id):
    with open('app/assets/products.json') as json_files:
        products = json.load(json_files)['response']['jsonBody']
    
    for i in products:
      if i['id'] == id:
        product = i
    
    try:
      product['name'] = product['name'].lower().split(' ')
      product['name'][1] = product['name'][1][0:-1]
      product['name'] = '-'.join(product['name'])
      
      file = product['name']
      with open(f'app/assets/{file}.json') as json_file:
        product = json.load(json_file)['response']['jsonBody']

      return jsonify(product)
    except UnboundLocalError:
      return  {"error": "Product not found"},404
   
    
  


def generate_bill():
    data = request.json
    total_price = 0
    total_disccount =  0
    try:
      for i in data:
        if len(i['promotions']) != 0:
          for promo in i['promotions']:
            all_products_price = i['price'] * i['quantity']
            product_disccount = 0

            if promo['type'] == 'QTY_BASED_PRICE_OVERRIDE':
              result = floor(i['quantity'])/promo['required_qty']
              result = floor(result)
              product_disccount += result * promo['price']

            if promo['type'] == 'BUY_X_GET_Y_FREE':
              result = floor(i['quantity'] / promo['required_qty'])
              quantity_free = result * promo['free_qty']
              product_disccount += quantity_free * i['price']
            if promo['type'] == 'FLAT_PERCENT':
              product_disccount += all_products_price / promo['amount']

            total_disccount += product_disccount
        total_price += i['price'] * i['quantity']

      
      output = {
        "total_price" : total_price,
        "total_disccount" : total_disccount,
        "total_spent": total_price - total_disccount
        }
      return output, 200
    except KeyError as e:
        return {"error": f"missing keys {e.args[0]}"},404
