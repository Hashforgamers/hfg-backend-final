from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, Date, Time
from sqlalchemy.orm import relationship
from flask_sqlalchemy import SQLAlchemy
from . import db  # Import db from the models package

# AvailableGame model
class AvailableGame(db.Model):
    __tablename__ = 'available_games'
    
    id = Column(Integer, primary_key=True)
    vendor_id = Column(Integer, ForeignKey('vendors.id'), nullable=False)
    game_name = Column(String(50), nullable=False)
    total_slot = Column(Integer, nullable=False)
    single_slot_price = Column(Integer, nullable=False)

    vendor = relationship('Vendor', back_populates='available_games')
