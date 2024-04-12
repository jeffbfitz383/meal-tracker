from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.orm import validates
from config import *
from flask_bcrypt import Bcrypt
from sqlalchemy.ext.hybrid import hybrid_property
bcrypt = Bcrypt()


# Models go here!
