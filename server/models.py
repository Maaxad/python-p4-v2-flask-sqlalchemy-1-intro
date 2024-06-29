from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData

# contains definitions of tables and associated schema constructs
metadata = MetaData()

# create the Flask SQLAlchemy extension
db = SQLAlchemy(metadata=metadata)

# define a model class by inheriting from db.Model.


class Pet(db.Model):
    __tablename__ = 'pets'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    species = db.Column(db.String)

class user(db.model):
    __tablename__= 'users'
    id = db.Column(db.integer, primary_key=True)
    username = db.column(db.string(80), unique=True, nullable=False, index=True)
    email = db.column(db.string(120), unique=True)
    verified = db.column(db.Boolean, default=False)