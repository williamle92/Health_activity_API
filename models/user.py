from db import db



class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.Text(), nullable=False)
    healthlogs = db.relationship('HealthLogModel', backref='User', lazy="dynamic")
    activitylogs = db.relationship('ActivityLog', backref='User', lazy="dynamic")

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def json(self):
        return {"type": "user", 'username': self.username, 'id': self.id, "email":self.email, "health logs": [health.json() for health in self.healthlogs.all()], "activity logs": [a.json() for a in self.activitylogs.all()]}

    @classmethod
    def find_by_username(self, username):
        return User.query.filter_by(username=username).first()
    

