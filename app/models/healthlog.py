from app import db


class HealthLog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    weight_in_pounds = db.Column(db.Integer, nullabe=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullabe=False)

    def __init__(self, weight_in_pounds):
        self.weight_in_pounds = weight_in_pounds
       




