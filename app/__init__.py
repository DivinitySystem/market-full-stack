from flask import Flask
from app import routes
from app.configs import app_config, database, migration, auth_jwt
from flask_cors import CORS


def create_app():
    app = Flask(__name__)
    CORS(app)
    app_config.init_app(app)
    database.init_app(app)
    migration.init_app(app)
    routes.init_app(app)
    auth_jwt.init_app(app)
    return app
