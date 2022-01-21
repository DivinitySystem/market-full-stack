from app.exc.exc import InvalidTokenError


def key_validator(valid_keys, data):
    """

        Returns a dict with the data if the keys are in valid keys
        
        Else raises a KeyError with the invalid data

    """
    new_data = {}
    invalid_data = []
    for key in valid_keys:
        if key not in data:
            invalid_data.append(key)
        else:
            new_data[key] = data[key]

    if len(invalid_data) > 0:
        raise KeyError(f"{invalid_data}")
    
    return new_data


def patch_itens(keys, data):
    valid_keys = {}
    for key, value in data.items(): 
        if key in keys:
            valid_keys[key] = value
    
    if len(valid_keys) == 0: raise KeyError
    return valid_keys

def verify_token(token_email, email):
    
    if not token_email == email:
        raise InvalidTokenError