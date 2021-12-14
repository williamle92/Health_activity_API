from flask import Flask
from resources.activitylog import Activities, ActivityLogResource
from resources.healthlog import HealthLogList, HealthLogResource
from resources.user import UserRegister, UserList, UserResource
from db import db
from config import Config
from flask_migrate import Migrate
from flask_restful import Api


app = Flask(__name__)
app.config.from_object(Config)
migrate = Migrate(app, db)
db.init_app(app)
api = Api(app)



# API endpoints
api.add_resource(UserRegister, '/register')
api.add_resource(UserList, '/users')
api.add_resource(UserResource, "/user/<id>")
api.add_resource(HealthLogResource,'/health', "/health/<id>")
api.add_resource(HealthLogList, '/healthlogs')
api.add_resource(ActivityLogResource, '/activity/<id>', '/activity')
api.add_resource(Activities, "/activities")

def create_app(Config):
    app= Flask(__name__)
    



if __name__ == "__main__":
    from db import db
    db.init_app(app)
    app.run(port=5000, debug=True)