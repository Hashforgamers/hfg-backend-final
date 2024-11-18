from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import relationship
from . import db

class User(db.Model):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    fid = Column(String(255), unique=True, nullable=False)
    avatar_path = Column(String(255), nullable=True)
    name = Column(String(255), nullable=False)
    gender = Column(String(50), nullable=True)
    dob = Column(Date, nullable=True)
    game_username = Column(String(255), unique=True, nullable=False)

    # Relationships
    physical_address = relationship(
        'PhysicalAddress',
        primaryjoin="and_(PhysicalAddress.parent_id==User.id, "
                    "PhysicalAddress.parent_type=='user')",
        uselist=False,
        cascade="all, delete-orphan"
    )
    contact_info = relationship(
        'ContactInfo',
        primaryjoin="and_(ContactInfo.parent_id==User.id, "
                    "ContactInfo.parent_type=='user')",
        uselist=False,
        cascade="all, delete-orphan"
    )
