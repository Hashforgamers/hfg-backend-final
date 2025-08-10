# HashWalletTransaction Model

## Description
Tracks all financial transactions affecting user HashWallet balances (credits/debits).

## Fields

| Field | Type | Constraints | Description |
|-------|------|------------|-------------|
| id | Integer | Primary Key | Unique identifier |
| user_id | Integer | FK, Not Null | User involved in transaction |
| amount | Integer | Not Null | Transaction amount (signed) |
| type | String(50) | Nullable | Transaction category |
| reference_id | String(50) | Nullable | Related entity ID |
| timestamp | DateTime | Default=Current Time | When transaction occurred |

## Transaction Types
- `booking`: Slot booking payment
- `top-up`: Wallet recharge  
- `admin-credit`: Manual adjustment
- `refund`: Booking cancellation
- `referral`: Referral bonus

## Example Usage
```python
# Record a booking payment
tx = HashWalletTransaction(
    user_id=123,
    amount=-500,
    type="booking",
    reference_id="BOOK-456"
)

# Get user transaction history
history = HashWalletTransaction.query.filter_by(
    user_id=123
).order_by(HashWalletTransaction.timestamp.desc()).all()