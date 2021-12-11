from app import db


class ActivityLog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    activity = db.Column(db.String(100))
    scale = db.Column(db.Integer)
    time = db.Column(db.Integer)
    description = db.Column(db.String(300))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullabe=False)

    def __iniit__(self, activity, rating, time, description):
        self.activity = activity
        self.rating = rating
        self.time = time
        self.description = description
