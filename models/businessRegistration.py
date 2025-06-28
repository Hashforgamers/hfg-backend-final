from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, Date, Time
from sqlalchemy.orm import relationship
from flask_sqlalchemy import SQLAlchemy
from extension import db  # Import db from the models package

# BusinessRegistration model
class BusinessRegistration(db.Model):
    __tablename__ = 'business_registration'
    
    id = Column(Integer, primary_key=True)
    registration_number = Column(String(100), nullable=False)
    registration_date = Column(Date, nullable=False)

    vendors = relationship('Vendor', back_populates='business_registration')

