# models/slot.py
from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, Date
from sqlalchemy.orm import relationship
from . import db

class Slot(db.Model):
    __tablename__ = 'slots'

    id = db.Column(db.Integer, primary_key=True)
    gaming_type = db.Column(db.String(50), nullable=False)
    time_bracket = db.Column(db.String(100), nullable=False)
    date = db.Column(db.Date, nullable=False)
    is_available = db.Column(db.Boolean, default=True)

    # Relationship with Booking (one-to-many)
    bookings = relationship('Booking', back_populates='slot')

    def __repr__(self):
        return f"<Slot gaming_type={self.gaming_type} time_bracket={self.time_bracket}>"
