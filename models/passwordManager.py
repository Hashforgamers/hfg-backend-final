from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from . import db
from sqlalchemy.ext.declarative import declared_attr

class PasswordManager(db.Model):
    __tablename__ = 'password_manager'

    id = Column(Integer, primary_key=True)
    userid = Column(String(255), nullable=False)
    password = Column(String(255), nullable=False)

    # Parent relationship columns
    parent_id = Column(Integer, nullable=False)
    parent_type = Column(String(50), nullable=False)

    # Polymorphic setup
    @declared_attr
    def __mapper_args__(cls):
        return {
            'polymorphic_on': cls.parent_type,
            'polymorphic_identity': 'password_manager'
        }

    # Relationships using @declared_attr
    @declared_attr
    def user(cls):
        return relationship(
            'User',
            primaryjoin="and_(PasswordManager.parent_id == User.id, PasswordManager.parent_type == 'user')",
            back_populates='password'
        )

    @declared_attr
    def vendor(cls):
        return relationship(
            'Vendor',
            primaryjoin="and_(PasswordManager.parent_id == Vendor.id, PasswordManager.parent_type == 'vendor')",
            back_populates='password'
        )
