from flask_restful import Resource
from flask import Response, request
import model.db_management as dbm
import model.utils as utils

get_user = """
            SELECT user_id, user_password, user_salt
            FROM SESSION.USERS
            WHERE user_email = %s
        """

class Authenticate(Resource):

    def post(self):
        if all(key in request.json for key in ('email', 'password')):
            email = request.json['email']
            password = request.json['password']

            db = dbm.Database()
            user = db.select_first(get_user, [email])

            if user is None:
                return Response(status=401)
            
            salt, hashed_pwd = utils.hash_password(password, user['user_salt'])

            if hashed_pwd == user['user_password']:
                return {'token': utils.gen_jwt(user['user_id'])}
            else:
                return Response(status=401)
        else:
            return Response(status=412)


insert_user = """
                INSERT INTO SESSION.USERS(user_email, user_name, user_password, user_salt)
                VALUES(%s, %s, %s, %s)
            """

class Register(Resource):

    def get(self):
        db = dbm.Database()
        return db.select("SELECT * FROM SESSION.USERS")

    def post(self):
        if all(key in request.json for key in ('email', 'name', 'password')):
            email = request.json['email']
            name = request.json['name']
            password = request.json['password']
            salt, hashed_pwd = utils.hash_password(password)

            db = dbm.Database()
            db.insert(insert_user, [email, name, hashed_pwd, salt])

            return Response("Done", status=200)
        else:
            return Response("Missing args", status=412)


insert_user = """
                INSERT INTO SESSION.USERS(user_email, user_name, user_ext_con_type, user_ext_con_id)
                VALUES(%s, %s, %s, %s)
                RETURNING user_id
            """

check_if_user_exists = """
            SELECT user_id
            FROM SESSION.USERS
            WHERE user_ext_con_type = %s
            AND user_ext_con_id = %s
        """

class ExtAuth(Resource):

    def post(self):
        if all(key in request.json for key in ('ext_con_type', 'ext_con_id')):
            c_type = request.json['ext_con_type']
            c_id = request.json['ext_con_id']

            db = dbm.Database()


            if c_type == "GOOGLE":
                jwt = utils.decode_ext_jwt(c_id)
                acc = db.select_first(check_if_user_exists, [c_type, jwt["sub"]])
                if acc is None:
                    id = db.insert_returning_id(insert_user, [jwt["email"], jwt["name"], c_type, jwt["sub"]])
                else:
                    id = acc["user_id"]
            else:
                return Response("Wrong external connection type", status=412)


            return {'token': utils.gen_jwt(id)}
        else:
            return Response("Missing args", status=412)
