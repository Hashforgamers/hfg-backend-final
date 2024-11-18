from sqlalchemy import Column, Integer, String, Date, ForeignKey, JSON, Boolean
from sqlalchemy.orm import relationship
from . import db

class User(db.Model):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    fid = Column(String(255), unique=True, nullable=False)
    avatar_path = Column(String(255), nullable=True)
    name = Column(String(255), nullable=False)
    gender = Column(String(50), nullable=True)
    dob = Column(Date, nullable=True)
    game_username = Column(String(255), unique=True, nullable=False)

    # Relationships
    physical_address = relationship('PhysicalAddress', back_populates='users', uselist=False, cascade="all, delete-orphan")
    contact_info = relationship('ContactInfo', back_populates='users', uselist=False, cascade="all, delete-orphan")