# models/game.py
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from . import db 

class Game(db.Model):
    __tablename__ = 'games'

    id = Column(Integer, primary_key=True)
    name = Column(String(255), unique=True, nullable=False)

    # One-to-Many: One game can be supported by many vendors
    supported_by = relationship('SupportedGame', back_populates='game', cascade="all, delete-orphan")
