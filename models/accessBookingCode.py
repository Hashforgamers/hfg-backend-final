from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from . import db
from datetime import datetime

class AccessBookingCode(db.Model):
    __tablename__ = 'access_booking_codes'

    id = Column(Integer, primary_key=True)
    access_code = Column(String(6), unique=True, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    bookings = db.relationship('Booking', back_populates='access_code_entry')
