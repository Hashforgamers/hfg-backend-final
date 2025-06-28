from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, Date, Time
from sqlalchemy.orm import relationship
from flask_sqlalchemy import SQLAlchemy
from extension import db # Import db from the models package

# OpeningDay model
class OpeningDay(db.Model):
    __tablename__ = 'opening_days'
    
    id = Column(Integer, primary_key=True)
    vendor_id = Column(Integer, ForeignKey('vendors.id'), nullable=False)
    day = Column(String(10), nullable=False)  # e.g., 'mon', 'tues', etc.
    is_open = Column(Boolean, default=False)

    vendor = relationship('Vendor', back_populates='opening_days')

