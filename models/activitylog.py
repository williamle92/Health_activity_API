from db import db


class ActivityLog(db.Model):
    """
    Activity Log Flask-SQLAlchemy Model
    Represents objects contained in Activity Log table
    """
    id = db.Column(db.Integer, primary_key=True)
    activity = db.Column(db.String(100))
    scale = db.Column(db.Integer)
    time = db.Column(db.Integer)
    description = db.Column(db.String(300))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullabe=False)
    user = db.relationship('User')
    def __iniit__(self, activity, rating, time, description):
        self.activity = activity
        self.rating = rating
        self.time = time
        self.description = description


    def save_to_db(self):
        db.session.add()
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()