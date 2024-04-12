from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.orm import validates
from config import *
from flask_bcrypt import Bcrypt
from sqlalchemy.ext.hybrid import hybrid_property
bcrypt = Bcrypt()

class User(db.Model):
    __tablename__= "users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)

# Models go here!
