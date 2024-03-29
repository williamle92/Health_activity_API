from flask_restful import Resource, reqparse
from models.user import User



class UserRegister(Resource):
    # Parses the request and makes sure it has the required argument
    parser = reqparse.RequestParser()
    parser.add_argument('username',
                        type=str,
                        required=True,
                        help="Must contain a username"
                        )
    parser.add_argument('password',
                        type=str,
                        required=True,
                        help="Must contain a password"
                        )
    parser.add_argument('email',
                        type=str,
                        required=True,
                        help="Can not register without an email"
                        )

    def post(self):
        data = UserRegister.parser.parse_args()
        if User.find_by_username(data['username']):
            return {"Message": "There is already an existing username"}

        user = User(**data)
        user.save_to_db()
        return {"Message": "User created successfully"}, 201

class UserResource(Resource):    
    def get(self, id):
        user = User.query.filter_by(id=id).first()
        if user:
            return user.json()
        return {"Message": "The user searched by user ID does not exist"}

# Grabs a list of all the users
class UserList(Resource):
    def get(self):
        return {"data": [user.json() for user in User.query.all()]}