from db import db



class User(db.Model):
    """
    User Flask-SQLAlchemy Model
    Represents user objects in table: user
    """
    __tablename__ = "userinfo"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.Text(), nullable=False)
    healthlogs = db.relationship('HealthLogModel', backref='userinfo', lazy="dynamic")
    activitylogs = db.relationship('ActivityLog', backref='userinfo', lazy="dynamic")


    # When instantiating the user class, it requires username, email and password parameter
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

    # Method to save to the database
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    # Returns the response in JSON format
    def json(self):
        return {"type": "user", 'username': self.username, 'id': self.id, "email":self.email, "health logs": [health.json() for health in self.healthlogs.all()], "activity logs": [a.json() for a in self.activitylogs.all()]}

    # Class decorator allows classes to perform method on the class itself rather than instantiating the class
    @classmethod
    def find_by_username(self, username):
        return User.query.filter_by(username=username).first()
    
    # Representation of the object as a string. 
    def __repr__(self):
        return f"username: {self.username} email: {self.email}" 

