from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, Date, Time
from sqlalchemy.orm import relationship
from flask_sqlalchemy import SQLAlchemy
from . import db  # Import db from the models package

# Amenity model
class Amenity(db.Model):
    __tablename__ = 'amenities'
    
    id = Column(Integer, primary_key=True)
    vendor_id = Column(Integer, ForeignKey('vendors.id'), nullable=False)
    name = Column(String(50), nullable=False)
    available = Column(Boolean, default=False)

    vendor = relationship('Vendor', back_populates='amenities')