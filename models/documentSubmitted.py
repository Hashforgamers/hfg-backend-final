from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, Date, Time
from sqlalchemy.orm import relationship
from flask_sqlalchemy import SQLAlchemy

from . import db  # Import db from the models package

# DocumentSubmitted model
class DocumentSubmitted(db.Model):
    __tablename__ = 'documents_submitted'
    
    id = Column(Integer, primary_key=True)
    vendor_id = Column(Integer, ForeignKey('vendors.id'), nullable=False)
    document_name = Column(String(50), nullable=False)
    submitted = Column(Boolean, default=False)

    vendor = relationship('Vendor', back_populates='documents_submitted')
