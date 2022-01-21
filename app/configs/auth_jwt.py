from flask_jwt_extended import JWTManager
from flask import Flask
from datetime import timedelta
from os import environ

def init_app(app:Flask):
    app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=24)
    app.config["JWT_REFRESH_TOKEN_EXPIRES"] = timedelta(days=30)
    app.config['SECRET_KEY'] = environ.get("SECRET_KEY")    

    JWTManager(app)
