from dataclasses import dataclass
from sqlalchemy.orm import validates
from app.configs.database import db
from werkzeug.security import generate_password_hash,check_password_hash
import re

@dataclass
class User(db.Model):
    id: int
    nick_name: str
    email:str    

    __tablename__ = 'users'
    

    id = db.Column(db.Integer, primary_key=True)
    nick_name = db.Column(db.String(100), nullable=False, unique=True)
    email = db.Column(db.String(100), nullable=False, unique=True)
    password_hash = db.Column(db.String)  

    user_keys = ['nick_name', 'email', 'password']

    @validates('email')
    def validate_email(self,_,email):
        email_regex = r"^[\w-]+@[a-z\d]+\.[\w]{3}(.br)?"

        if not re.fullmatch(email_regex,email):
            raise ValueError("Invalid email, format should be equal to xxxx@xxxx.xxx.(xx)")
        return email
    
    @validates('nick_name')
    def validate_nick_name(self,_, nick_name):
        if type(nick_name) != str or len(nick_name) < 4:
            raise ValueError("Nick_name should have length > 4 and be a string")
        return nick_name
    
    @property
    def password(self):
        raise ValueError('password is not a readable attribute')
    
    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)
    
    
    def check_password(self, password_to_compare):
        return check_password_hash(self.password_hash, password_to_compare)
