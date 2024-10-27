from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, Date, Time
from sqlalchemy.orm import relationship
from flask_sqlalchemy import SQLAlchemy
from . import db  # Import db from the models package

# PhysicalAddress model
class PhysicalAddress(db.Model):
    __tablename__ = 'physical_address'
    
    id = Column(Integer, primary_key=True)
    address_type = Column(String(50), nullable=False)
    addressLine1 = Column(String(255), nullable=False)
    addressLine2 = Column(String(255), nullable=True)
    pincode = Column(String(10), nullable=False)
    state = Column(String(100), nullable=False)
    country = Column(String(100), nullable=False)
    is_active = Column(Boolean, default=True)
    latitude = Column(String(20), nullable=True)
    longitude = Column(String(20), nullable=True)

    vendors = relationship('Vendor', back_populates='physical_address')
