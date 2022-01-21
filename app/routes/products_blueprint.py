from flask import Blueprint
from app.controllers.products_controller import generate_bill, get_all_products, get_product_by_id

products_bp = Blueprint("food_bp", __name__, url_prefix="/products")


products_bp.get("")(get_all_products)
products_bp.post("")(generate_bill)
products_bp.get("/<id>")(get_product_by_id)