from flask import Blueprint
from app.controllers import user_controller

user_bp = Blueprint('user_bp', __name__ , url_prefix='/user')

user_bp.post('')(user_controller.post_user)
user_bp.delete('<int:id>')(user_controller.delete_user)
user_bp.patch('/<int:id>')(user_controller.patch_user)