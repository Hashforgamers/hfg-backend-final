# models/booking.py
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from . import db
from .availableGame import AvailableGame
from .slot import Slot

class Booking(db.Model):
    __tablename__ = 'bookings'
    
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, nullable=False)
    game_id = Column(Integer, ForeignKey('available_games.id'), nullable=False)
    slot_id = Column(Integer, ForeignKey('slots.id'), nullable=False)
    status = db.Column(db.String(20), default='pending_verified')  # New field for verification status
    

    # Relationship with AvailableGame (many-to-one)
    game = relationship('AvailableGame', back_populates='bookings')

    # Relationship with Slot (many-to-one)
    slot = relationship('Slot', back_populates='bookings')

    def __repr__(self):
        return f"<Booking user_id={self.user_id} game_id={self.game_id}>"
