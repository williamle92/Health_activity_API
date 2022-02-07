from db import db

class HealthLogModel(db.Model):
    """
    Health Log Flask-SQLAlchemy Model
    Represent a health log object in table: health_log_model
    """
    __tablename__ = "health"
    id = db.Column(db.Integer, primary_key=True)
    weight_in_pounds = db.Column(db.Integer, nullable=False)
    user_username = db.Column(db.String(80), db.ForeignKey('userinfo.username'), nullable=False)

    # Instantiates the class with the required parameters, weight in pounds and username
    def __init__(self, weight_in_pounds,user_username):
        self.weight_in_pounds = weight_in_pounds
        self.user_username = user_username
    
    # Returns a response in JSON format
    def json(self):
        return {"id":self.id,"weight in pounds": self.weight_in_pounds, "username": self.user_username}

    
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
    
    # Class decorator allows classes to perform method on the class itself rather than instantiating the class
    @classmethod
    def find_by_id(self, id):
        return HealthLogModel.query.filter_by(id=id).first()

    # Representation of the object as a string. 
    def __repr__(self):
        return f"Health Log \nweight in pounds: {self.weight_in_pounds}"
         



