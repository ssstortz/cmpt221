from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

# contains table objects
Base = declarative_base()

# NOTE: for the project, you will have to made a class in models.py for each table you
# have in db/schema
class User(Base):
    __tablename__ = 'Users'
    # NOTE: when using declarative base, we do NOT need db.Column, db.Integer, etc.
    UserID = Column(Integer,primary_key=True,autoincrement=True)
    FirstName = Column(String(40))
    LastName = Column(String(40))
    Email = Column(String(40))
    PhoneNumber = Column(String(12))
    Password = Column(String(256))

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
    