from flask import request, jsonify
from werkzeug.exceptions import NotFound
from app import controllers
from app.configs.database import db
from app.models.user_model import User
from sqlalchemy.exc import IntegrityError
from flask_jwt_extended import get_jwt, jwt_required
from app.exc.exc import InvalidTokenError


def post_user():
    data = request.json
    
    try:
        
        new_data = controllers.key_validator(User.user_keys, data)
        password_to_hash = new_data.pop('password')
        
        new_user = User(**new_data)
        new_user.password = password_to_hash
        
        db.session.add(new_user)
        db.session.commit()

        return jsonify(new_user),201
    
    except IntegrityError as e:
     
        return {"error": "User or Email already taken"},409

    except KeyError as e:
        return {
            "msg": f"Missing or Invalid data, {e.args[0]}",
            "Valid data": f"{User.user_keys}",  
        },400

    except ValueError as e:
        return {"error": e.args[0]},400
    

@jwt_required(locations=["headers"])
def delete_user(id):
    data = get_jwt()['sub']
   
    try:
        user = User.query.filter_by(id=id).first_or_404()
        controllers.verify_token(data['email'], user.email)
        db.session.delete(user)
        db.session.commit()
        return "",204
    except NotFound:
        return {"error": "User Not Found"},404
    except InvalidTokenError:
        return {"error": "Invalid Token"},401

@jwt_required(locations=["headers"])
def patch_user(id):
    token_data = get_jwt()['sub']
    try:
        user =  User.query.filter_by(id=id).first_or_404()
        data = request.json
        valid_data = controllers.patch_itens(User.user_keys, data)
        controllers.verify_token(token_data['email'], user.email)
        
        if 'password' in valid_data: valid_data.pop('password')
       
        for key, value in valid_data.items():
            setattr(user,key,value)
        
        db.session.commit()
        return valid_data,202

    except KeyError as e:
         return {
            "msg": f"Missing or Invalid data, {e.args[0]}",
        },400

    except NotFound:
        return {"error": "User not found"}, 404

    except ValueError as e:
        return {"error": e.args[0]},400
    
    except IntegrityError as e:
        return {"error": "User or Email already taken"},409
    except InvalidTokenError:
        return {"error": "Invalid Token"},401