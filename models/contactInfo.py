from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, Date, Time
from sqlalchemy.orm import relationship
from flask_sqlalchemy import SQLAlchemy

from . import db  # Import db from the models package

class ContactInfo(db.Model):
    __tablename__ = 'contact_info'
    
    id = Column(Integer, primary_key=True)
    email = Column(String(255), nullable=False)
    phone = Column(String(50), nullable=False)
    
    vendors = relationship('Vendor', back_populates='contact_info')
    users = relationship('User', back_populates='contact_info')
