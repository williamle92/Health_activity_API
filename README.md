# Health and activity tracker REST API with Flask:
## About the Project
This API was design to to track health and activity/excercises for each user. You can only create users, the update and delete function were removed to moderate data deletion. Each activity log and health log must be assigned with a user.  
![ERD](/src/ERD.png "ERD Diagram")

**Note this project was created using a .env file, and will need a separate .env to run. 
## Getting Started
This application is deployed on heroku: [Health Activity API](https://activity-rest-api.herokuapp.com/). Please view the API documentation to get started [API Documentation](https://documenter.getpostman.com/view/15868454/UVR7JnLC)

## Installation to use on local machine:

1. Pull files from repository.
``` 
git clone https://github.com/williamle92/Health_activity_API.git 
```
2. Optional: Create a virtual environment using 
```
python -m venv venv
```
3. To install all dependencies to project
```
pip install -r requirements.txt
```
4. Create a .env file
5. Link database url: "postgresql://scott:tiger@localhost/mydatabase", for more information please visit: [Flask-SQLAlchemy Configurations](https://flask-sqlalchemy.palletsprojects.com/en/2.x/config/)
6. Set up database "flask db init"
7. migrate "flask db migrate"
8. Upgrade: "flask db upgrade"



