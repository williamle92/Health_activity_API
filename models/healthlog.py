from db import db

class HealthLogModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    weight_in_pounds = db.Column(db.Integer, nullabe=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullabe=False)
    user = db.relationship("User")

    def __init__(self, weight_in_pounds,user_id):
        self.weight_in_pounds = weight_in_pounds
        self.user_id = user_id
    
    def json(self):
        return {"data": {"weight in pounds": self.weight_in_pounds, "user id": self.user_id}}

       
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
    
    def find_by_id(self, user_id):
        return HealthLogModel.query.filter_by(user_id=user_id).first()

    def __repr__(self):
        return f"Health Log \nweight in pounds: {self.weight_in_pounds}"
         



