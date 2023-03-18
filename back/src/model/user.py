from flask_restful import Resource
from flask import Response, request
import model.db_management as dbm
import model.utils as utils

get_user = """
            SELECT user_email, user_name
            FROM SESSION.USERS
            WHERE user_id = %s
        """

class User(Resource):

    def get(self):
        token = utils.verify_token(request.headers.get("Authorization"))
        if "error" in token:
            return Response(status=token["error"])
        
        db = dbm.Database()
        result = db.select_first(get_user, [token['id']])
        return result