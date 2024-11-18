from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from . import db

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
    
    # Polymorphic fields
    parent_id = Column(Integer, nullable=False)
    parent_type = Column(String(50), nullable=False)

    __mapper_args__ = {
        'polymorphic_identity': 'physical_address',
        'polymorphic_on': parent_type
    }
