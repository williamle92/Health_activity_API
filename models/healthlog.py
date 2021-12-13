from db import db

class HealthLogModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    weight_in_pounds = db.Column(db.Integer, nullable=False)
    user_username = db.Column(db.String(60), db.ForeignKey('user.username'), nullable=False)
    users = db.relationship("User")

    def __init__(self, weight_in_pounds,user_username):
        self.weight_in_pounds = weight_in_pounds
        self.user_username = user_username
    
    def json(self):
        return {"id":self.id,"weight in pounds": self.weight_in_pounds, "username": self.user_username}

       
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
    
    @classmethod
    def find_by_id(self, id):
        return HealthLogModel.query.filter_by(id=id).first()

    def __repr__(self):
        return f"Health Log \nweight in pounds: {self.weight_in_pounds}"
         



