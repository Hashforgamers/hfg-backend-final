from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Sequence
from sqlalchemy.orm import relationship
from . import db  # Import db from the models package
from datetime import datetime



# Vendor model
class Vendor(db.Model):
    __tablename__ = 'vendors'
    
    id = Column(Integer, Sequence('vendor_id_seq', start=2000), primary_key=True)
    cafe_name = Column(String(255), nullable=False)
    owner_name = Column(String(255), nullable=False)
    description = Column(String(255), nullable=True)

    # Relationships
    physical_address = relationship(
        'PhysicalAddress',
        primaryjoin="and_(PhysicalAddress.parent_id==Vendor.id, "
                    "PhysicalAddress.parent_type=='vendor')",
        uselist=False,
        cascade="all, delete-orphan"
    )
    contact_info = relationship(
        "ContactInfo",
        back_populates="vendor",  # Ensure this matches the relationship in ContactInfo
        uselist=False,
        cascade="all, delete"
    )

    business_registration_id = Column(Integer, ForeignKey('business_registration.id'), nullable=True)
    timing_id = Column(Integer, ForeignKey('timing.id'), nullable=True)
    
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

    # In Vendor model
    account_id = Column(Integer, ForeignKey('vendor_accounts.id'), nullable=True)
    account = relationship('VendorAccount', back_populates='vendors')

    pin = relationship('VendorPin', back_populates='vendor', uselist=False, cascade="all, delete-orphan")

    # One-to-One relationship with PasswordManager

    password = relationship(
        'PasswordManager',
        primaryjoin="and_(foreign(PasswordManager.parent_id) == Vendor.id, PasswordManager.parent_type == 'vendor')",
        back_populates='vendor',
        uselist=False,
        cascade="all, delete-orphan"
    )

    # Add in Vendor model
    supported_games = relationship(
        'SupportedGame',
        back_populates='vendor',
        cascade="all, delete-orphan"
    )

    extra_service_categories = relationship('ExtraServiceCategory', back_populates='vendor', cascade='all, delete-orphan')

    # One-to-Many relationship with VendorStatus
    statuses = relationship('VendorStatus', back_populates='vendor', cascade="all, delete")

    # Add relationship to transactions
    transactions = relationship('Transaction', back_populates='vendor', cascade="all, delete-orphan")


