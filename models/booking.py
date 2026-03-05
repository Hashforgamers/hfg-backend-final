# models/booking.py
from sqlalchemy import Column, Integer, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from . import db
from datetime import datetime
import pytz

from .availableGame import AvailableGame
from .slot import Slot

# Helper function to return current IST time
def current_time_ist():
    return datetime.now(pytz.timezone("Asia/Kolkata"))

class Booking(db.Model):
    __tablename__ = 'bookings'
    
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, nullable=False)
    game_id = Column(Integer, ForeignKey('available_games.id'), nullable=False)
    slot_id = Column(Integer, ForeignKey('slots.id'), nullable=False)
    status = db.Column(db.String(20), default='pending_verified')

    # ✅ Auto timestamps with IST
    created_at = Column(DateTime(timezone=True), default=current_time_ist, nullable=False)
    updated_at = Column(DateTime(timezone=True), default=current_time_ist, onupdate=current_time_ist, nullable=False)

    # Relationships
    game = relationship('AvailableGame', back_populates='bookings')
    slot = relationship('Slot', back_populates='bookings')
    transaction = relationship('Transaction', back_populates='booking', uselist=False)
    booking_extra_services = relationship('BookingExtraService', back_populates='booking', cascade='all, delete-orphan')
    access_code_id = Column(Integer, ForeignKey('access_booking_codes.id'), nullable=True)
    access_code_entry = db.relationship('AccessBookingCode', back_populates='bookings')

    def __repr__(self):
        return f"<Booking user_id={self.user_id} game_id={self.game_id}>"
