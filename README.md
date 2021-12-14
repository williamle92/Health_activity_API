# Health and activity tracker REST API with Flask:
This API was design to create users, health logs and activity logs. There is CRUD functionality for the health logs and acitivity logs however, user are only limited to post and get methods. 

**Note this project was created using a .env file, and will need a separate .env to run. 

Steps to reproduce the same results:

1. Pull files from repository.
2. Optional: Create a virtual environment using "python -m venv venv
3. "pip install -r requirements.txt" to the venv
4. Create a .env file
5. Link database url: "postgresql://scott:tiger@localhost/mydatabase", for more information please visit: [Flask-SQLAlchemy Configurations](https://flask-sqlalchemy.palletsprojects.com/en/2.x/config/)
6. Set up database "flask db init"
7. migrate "flask db migrate"
8. Upgrade: "flask db upgrade"




API Documentation:
https://documenter.getpostman.com/view/15868454/UVR7JnLC