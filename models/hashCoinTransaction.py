# models/hash_coin_transaction.py

from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, Date, Time
from sqlalchemy.orm import relationship
from flask_sqlalchemy import SQLAlchemy
from models.user import User

from extension import db 

class HashCoinTransaction(db.Model):
    __tablename__ = 'hash_coin_transactions'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    coins_changed = Column(Integer, nullable=False)  # +1000 or -10000
    reason = Column(String(255))  # e.g., "Booking", "Voucher Redemption"
    timestamp = Column(DateTime, default=datetime.utcnow)

    user = db.relationship("User", backref="hash_coin_transactions")
