from flask import Response
import jwt
from google.auth import jwt as jwtg
import datetime
import bcrypt

SECRET = "heyheyhey"


def hash_password(password, salt=None):
    if salt is None:
        salt = bcrypt.gensalt()
    else:
        salt = salt.encode('utf8')
    hashed_password = bcrypt.hashpw(password.encode('utf8'), salt)
    return salt.decode(), hashed_password.decode()


def gen_jwt(id):
    json = {
        'id': id,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)
    }
    return jwt.encode(json, SECRET, algorithm='HS256')


def decode_jwt(token):
    return jwt.decode(token, SECRET, algorithms='HS256')

def decode_ext_jwt(token):
    return jwtg.decode(token, verify=False)


def verify_token(auth_header):
    if auth_header is None:
        return {"error": 412}
    auth_header = auth_header.split(" ")[1]
    try:
        return decode_jwt(auth_header)
    except jwt.exceptions.InvalidTokenError:
        return {"error": 401}
    except jwt.exceptions.ExpiredSignatureError:
        return {"error": 401}
