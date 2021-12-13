from flask_restful import Resource, reqparse
from models.activitylog import ActivityLog
from models.user import User


class ActivityLogResource(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('user_username',
    type=str,
    required=True,
    help="Must contain key: username in string format"
    )
    parser.add_argument('activity',
    type=str,
    required=True,
    help="Must contain key: activity in string format"
    )
    parser.add_argument('rating',
    type=str,
    required=True,
    help="Must contain key: rating in string format"
    )
    parser.add_argument('time_elapsed',
    type=int,
    required=True,
    help="must contain time_elapsed in int (minutes)"
    )
    parser.add_argument('description',
    type=str,
    required=True,
    help="Must contain key: description in string format"
    )

    def get(self, id):
        activitylog = ActivityLog.find_by_id(id)
        if not activitylog:
            return {"Message": "The activity log does not exist, please try searching by different ID"},404
        return activitylog.json(), 200

    def post(self):
        data = ActivityLogResource.parser.parse_args()
        userexist = User.find_by_username(data['user_username'])
        if not userexist:
            return {"message": "The user does not exist, please create a username before proceeding."}
        activitylog = ActivityLog(**data)
        try:
            activitylog.save_to_db()
        except:
            return {"Message": "An error occured while inserting the activity log "}, 500
        return activitylog.json(),201

    def delete(self, id):
        activitylog = ActivityLog.find_by_id(id)
        if activitylog:
            activitylog.delete_from_db()
        return {"message": "Activity log delete from database"}

    def put(self,id):
        data= ActivityLogResource.parser.parse_args()
        actvitiylog = ActivityLog.find_by_id(id)
        if not actvitiylog:
            actvitiylog= ActivityLog(**data)
        else:
            actvitiylog.activity = data['activity']
            actvitiylog.rating = data['rating']
            actvitiylog.time_elasped = data['time_elapsed']
            actvitiylog.description = data['description']
        actvitiylog.save_to_db()
        return actvitiylog.json()