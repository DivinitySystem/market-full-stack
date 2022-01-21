from flask import Blueprint
from app.controllers.login_controller import login

login_bp = Blueprint('login_bp', __name__,  url_prefix="/login")

login_bp.post("")(login)