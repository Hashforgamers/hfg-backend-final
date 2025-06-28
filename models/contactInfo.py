from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from . import db


class ContactInfo(db.Model):
    __tablename__ = 'contact_info'
    
    id = Column(Integer, primary_key=True)
    email = Column(String(255), nullable=False)
    phone = Column(String(50), nullable=False)
    
    # Generic parent relationship columns
    parent_id = Column(Integer, nullable=False)
    parent_type = Column(String(50), nullable=False)

    __mapper_args__ = {
        'polymorphic_on': 'parent_type',
        'polymorphic_identity': 'contact_info',
    }

    # Relationships
    user = relationship(
        "User",
        primaryjoin="and_(ContactInfo.parent_id == User.id, ContactInfo.parent_type == 'user')",
        back_populates="contact_info",
        uselist=False
    )

    vendor = relationship(
        "Vendor",
        primaryjoin="and_(ContactInfo.parent_id == Vendor.id, ContactInfo.parent_type == 'vendor')",
        back_populates="contact_info",
        uselist=False
    )
