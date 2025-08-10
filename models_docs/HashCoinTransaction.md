# HashCoinTransaction Model

## Description
Tracks transactions of the platform's cryptocurrency (HashCoins) between users and the system.

## Fields

| Field | Type | Constraints | Description |
|-------|------|------------|-------------|
| id | Integer | Primary Key | Unique identifier |
| user_id | Integer | FK, Not Null | User involved in transaction |
| coins_changed | Integer | Not Null | Amount changed (positve/negative) |
| reason | String(255) | Nullable | Transaction purpose/description |
| timestamp | DateTime | Default=Current Time | When transaction occurred |

## Relationships

- **user**: Associated User record (many-to-one via backref)

## Typical Transaction Reasons
- Booking payments
- Voucher redemptions  
- Referral rewards
- Admin adjustments

## Example Usage
```python
# Create transaction
tx = HashCoinTransaction(
    user_id=123,
    coins_changed=-500,
    reason="Slot booking payment"
)

# Get user transactions
transactions = HashCoinTransaction.query.filter_by(
    user_id=123
).order_by(HashCoinTransaction.timestamp.desc()).all()