from flask import Flask
from resources.user import UserRegister
from db import db


from config import Config
from flask_migrate import Migrate
from flask_restful import Api


app = Flask(__name__)
app.config.from_object(Config)
migrate = Migrate(app, db)
db.init_app(app)
api = Api(app)


@app.route("/")
def index():
    return "Hello world"


api.add_resource(UserRegister, '/register')


if __name__ == "__main__":
    from db import db
    db.init_app(app)
    app.run(port=5000, debug=True)