from flask_restful import Resource, reqparse
from models.healthlog import HealthLogModel
from models.user import User

class HealthLogResource(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("weight_in_pounds", 
    type=int,
    required=True,
    help="Must contain weight in pounds. Please use 'weight_in_pounds' as key"
    )
    parser.add_argument("user_username", 
    type= str,
    required=True,
    help="Must contain key: user_username in string format"
    )

    def get(self, id):
        healthlog = HealthLogModel.find_by_id(id)
        if healthlog:
            return healthlog.json()
        return {"messsage": "The health log could not be found"}, 404

    def post(self):
        data = HealthLogResource.parser.parse_args()
        user = User.find_by_username(data['user_username'])
        if not user:
            return {"message": "The user does not exist, please create a username before proceeding."}
        healthlog = HealthLogModel(**data)
        try:
            healthlog.save_to_db()
        except:
            return {"Message": "An error occured while inserting the health log "}
        return healthlog.json(), 201

    def delete(self, id):
        healthlog = HealthLogModel.find_by_id(id)
        if healthlog:
            healthlog.delete_from_db()
        return {'message': 'Item deleted'}

    def put(self, id):
        data = HealthLogResource.parser.parse_args()
        healthlog = HealthLogModel.find_by_id(id)

        if healthlog is None:
            healthlog = HealthLogModel(**data)
        else:
            healthlog.weight_in_pounds = data['weight_in_pounds']
        healthlog.save_to_db()
        return healthlog.json()

class HealthLogList(Resource):
    def get(self):
        return {"data": [x.json() for x in HealthLogModel.query.all()]}