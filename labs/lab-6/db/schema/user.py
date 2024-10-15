"""user.py: create a table named users"""
from db.server import db

class User(db.Model):
    __tablename__ = 'Users'
    UserID = db.Column(db.Integer,primary_key=True,autoincrement=True)
    FirstName = db.Column(db.String(40))
    LastName = db.Column(db.String(40))
    Email = db.Column(db.String(40))
    PhoneNumber = db.Column(db.String(12))
    Password = db.Column(db.String(256))

    def __init__(self, FirstName, LastName, Email, PhoneNumber, Password):
        self.FirstName = FirstName
        self.LastName = LastName
        self.Email = Email
        self.PhoneNumber = PhoneNumber
        self.Password = Password

    def __repr__(self):
        return f"""
            "FIRST NAME: {self.FirstName},
             LAST NAME: {self.LastName},
             EMAIL: {self.Email},
             PHONE NUMBER: {self.PhoneNumber},
             PASSWORD: {self.Password}
        """
    