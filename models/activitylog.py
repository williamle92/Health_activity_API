from db import db


class ActivityLog(db.Model):
    """
    Activity Log Flask-SQLAlchemy Model
    Represents objects contained in table: activity
    """
    __tablename__ = "activity"
    id = db.Column(db.Integer, primary_key=True)
    user_username = db.Column(db.String(80), db.ForeignKey('userinfo.username'), nullable=False)
    activity = db.Column(db.String(100))
    rating = db.Column(db.String(25))
    time_elapsed = db.Column(db.Integer)
    description = db.Column(db.String(300))

    # Instantiates an object with the required parameters, username, activity, rating time elapsed and description
    def __init__(self,user_username, activity, rating, time_elapsed, description):
        self.user_username =user_username
        self.activity = activity
        self.rating = rating
        self.time_elapsed = time_elapsed
        self.description = description

    # Returns a response in JSON format
    def json(self):
        return {"id": self.id, "username": self.user_username, "activity": self.activity, "rating": self.rating, 'time elapsed': self.time_elapsed, "description": self.description}

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()


     # Class decorator allows classes to perform method on the class itself rather than instantiating the class
    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id).first()

    # Representation of the object as a string.
    def __repr__(self):
        return f"**Activity Log ** \nusername: {self.user_username}\nActivity: {self.activity}\nrating: {self.rating}\ntime elapsed: {self.time_elapsed}\ndescription: {self.description}"