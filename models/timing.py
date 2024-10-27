from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, Date, Time
from sqlalchemy.orm import relationship
from flask_sqlalchemy import SQLAlchemy
from . import db  # Import db from the models package

# Timing model
class Timing(db.Model):
    __tablename__ = 'timing'
    
    id = Column(Integer, primary_key=True)
    opening_time = Column(Time, nullable=False)
    closing_time = Column(Time, nullable=False)

    vendors = relationship('Vendor', back_populates='timing')

