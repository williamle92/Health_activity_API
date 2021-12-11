from app import db



class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.Text(), nullable=False)
    healthlogs = db.relationship('HealthLog', backref='user', lazy=True)
    activitylogs = db.relationship('ActivityLog', backref='user', lazy=True)
    