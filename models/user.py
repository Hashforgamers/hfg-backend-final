from sqlalchemy import Column, Integer, String, Date, Sequence, ForeignKey
from sqlalchemy.orm import relationship
from extension import db



class User(db.Model):
    __tablename__ = 'users'
    
    id = Column(Integer, Sequence('user_id_seq', start=2000), primary_key=True)
    fid = Column(String(255), unique=True, nullable=False)
    avatar_path = Column(String(255), nullable=True)
    name = Column(String(255), nullable=False)
    gender = Column(String(50), nullable=True)
    dob = Column(Date, nullable=True)
    game_username = Column(String(255), unique=True, nullable=False)

    referral_code = Column(String(10), unique=True)
    referred_by = Column(String(10), ForeignKey('users.referral_code'), nullable=True)
    referral_rewards = Column(Integer, default=0)
    
    # Adding the parent_type column explicitly
    parent_type = Column(String(50), nullable=False, default='user')

    # Relationships
    physical_address = relationship(
        'PhysicalAddress',
        primaryjoin="and_(PhysicalAddress.parent_id==User.id, "
                    "PhysicalAddress.parent_type=='user')",
        uselist=False,
        cascade="all, delete-orphan"
    )

    contact_info = relationship(
        "ContactInfo",
        back_populates="user",  # Ensure this matches the relationship in ContactInfo
        uselist=False,
        cascade="all, delete"
    )    
    
    # One-to-One relationship with PasswordManager
    password = relationship(
        'PasswordManager',
        primaryjoin="and_(foreign(PasswordManager.parent_id) == User.id, PasswordManager.parent_type == 'user')",
        back_populates='user',
        uselist=False,
        cascade="all, delete-orphan"
    )
