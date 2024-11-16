from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from . import db  # Import db from the models package
from datetime import datetime

# Vendor model
class Vendor(db.Model):
    __tablename__ = 'vendors'
    
    id = Column(Integer, primary_key=True)
    cafe_name = Column(String(255), nullable=False)
    owner_name = Column(String(255), nullable=False)
    description = Column(String(255), nullable=True)

    contact_info_id = Column(Integer, ForeignKey('contact_info.id'), nullable=False)
    physical_address_id = Column(Integer, ForeignKey('physical_address.id'), nullable=False)
    business_registration_id = Column(Integer, ForeignKey('business_registration.id'), nullable=False)
    timing_id = Column(Integer, ForeignKey('timing.id'), nullable=False)
    
    # Timestamps
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationships
    contact_info = relationship('ContactInfo', back_populates='vendors')
    physical_address = relationship('PhysicalAddress', back_populates='vendors')
    business_registration = relationship('BusinessRegistration', back_populates='vendors')
    timing = relationship('Timing', back_populates='vendors')
    
    amenities = relationship('Amenity', back_populates='vendor', cascade="all, delete-orphan")
    documents_submitted = relationship('DocumentSubmitted', back_populates='vendor', cascade="all, delete-orphan")
    opening_days = relationship('OpeningDay', back_populates='vendor', cascade="all, delete-orphan")
    available_games = relationship('AvailableGame', back_populates='vendor', cascade="all, delete-orphan")

    # One-to-One relationship with VendorCredential
    credential = relationship('VendorCredential', uselist=False, back_populates='vendor', cascade="all, delete")

    # One-to-Many relationship with VendorStatus
    statuses = relationship('VendorStatus', back_populates='vendor', cascade="all, delete")
