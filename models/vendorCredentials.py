# models/vendorCredentials.py
# from sqlalchemy import Column, Integer, String, ForeignKey
# from sqlalchemy.orm import relationship
# from . import db

# class VendorCredential(db.Model):
#     __tablename__ = 'vendor_credentials'
    
#     id = Column(Integer, primary_key=True)
#     vendor_id = Column(Integer, ForeignKey('vendors.id'), nullable=False, unique=True)
#     username = Column(String, nullable=False, unique=True)
#     password_hash = Column(String, nullable=False)

#     # Link to Vendor model
#     vendor = relationship('Vendor', back_populates='credential')