from flask_restful import Resource, reqparse
from models.user import User



class UserRegister(Resource):
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
            return {"message": "There is already an existing username"}

    
        user = User(**data)
        user.save_to_db()
        return {"Message": "User created successfully"}, 201
