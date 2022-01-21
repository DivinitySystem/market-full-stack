from flask import Flask
from app.routes.api_blueprint import api_bp
def init_app(app: Flask):
    
    

    app.register_blueprint(api_bp)