from flask import request, jsonify
from app.exc.exc import InvalidPasswordError
from app.models.user_model import User
from werkzeug.exceptions import NotFound
from flask_jwt_extended import create_access_token


def login():   

    try:
        email = request.json['email']
        password = request.json['password']
        user = User.query.filter_by(email=email).first_or_404()
        if not user.check_password(password):
            raise InvalidPasswordError
        acces_token = create_access_token(user)
        return jsonify({"token": acces_token})


    except InvalidPasswordError:
        return {"error": "Invalid password"},401

    except NotFound:
        return {"error": "User not found"},404
    
    except KeyError:
        return {"error": "Missing key, email and password required"},400