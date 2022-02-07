from flask import Flask
from resources.activitylog import Activities, ActivityLogResource
from resources.healthlog import HealthLogList, HealthLogResource
from resources.user import UserRegister, UserList, UserResource
from db import db
from config import Config
from flask_migrate import Migrate
from flask_restful import Api

# Instantiate Flask app
app = Flask(__name__)

# Setting configurations from Config object 
app.config.from_object(Config)

# Instantiate migrate object
migrate = Migrate(app, db)

# Instantiate db
db.init_app(app)

# Instantiate API object
api = Api(app)



# API endpoints
api.add_resource(UserRegister, '/register')
api.add_resource(UserList, '/users')
api.add_resource(UserResource, "/user/<id>")
api.add_resource(HealthLogResource,'/health', "/health/<id>")
api.add_resource(HealthLogList, '/healthlogs')
api.add_resource(ActivityLogResource, '/activity/<id>', '/activity')
api.add_resource(Activities, "/activities")


# App factory 
def create_app(config_class=Config):
    app= Flask(__name__)
    app.config.from_object(config_class)
    db.init_app(app)
    migrate.init_app(app, db)
    return app

with app.app_context():
    db.create_all()


if __name__ == "__main__":
    from db import db
    db.init_app(app)
    app.run(port=5000, debug=True)