# models/available_game.py
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from . import db

class AvailableGame(db.Model):
    __tablename__ = 'available_games'
    
    id = Column(Integer, primary_key=True)
    vendor_id = Column(Integer, ForeignKey('vendors.id'), nullable=False)
    game_name = Column(String(50), nullable=False)
    total_slot = Column(Integer, nullable=False)
    single_slot_price = Column(Integer, nullable=False)

    # Relationship with Vendor (one-to-many)
    vendor = relationship('Vendor', back_populates='available_games')
    
    # Relationship with Booking (one-to-many)
    bookings = relationship('Booking', back_populates='game')

    def __repr__(self):
        return f"<AvailableGame game_name={self.game_name} vendor_id={self.vendor_id}>"
