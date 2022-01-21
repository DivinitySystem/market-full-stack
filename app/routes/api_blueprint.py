from flask import Blueprint
from app.routes.user_blueprint import user_bp
from app.routes.products_blueprint import products_bp
from app.routes.login_blueprint import login_bp

api_bp = Blueprint("api_bp", __name__)


api_bp.register_blueprint(user_bp)
api_bp.register_blueprint(products_bp)
api_bp.register_blueprint(login_bp)

