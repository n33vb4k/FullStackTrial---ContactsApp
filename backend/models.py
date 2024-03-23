from config import db

#creating contact class that extends db.Model so we can quiery etc.
class Contact(db.Model):
    id = db.Column(db.Integer, primary_key =True)
    first_name = db.Column(db.String(80), unique=False, nullable=False)
    last_name = db.Column(db.String(80), unique=False, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    #returns the database in json format
    def to_json(self):
        return {
            "id": self.id,
            "firstName": self.first_name,
            "lastName": self.last_name,
            "email": self.email,
        }


