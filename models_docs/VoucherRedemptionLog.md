# VoucherRedemptionLog Model

## Description
Tracks voucher usage history and associations.

## Fields

| Field | Type | Constraints | Description |
|-------|------|-------------|-------------|
| id | Integer | PK | Log entry ID |
| user_id | Integer | FK, Not Null | Redeeming user |
| voucher_id | Integer | FK, Not Null | Voucher used |
| booking_id | Integer | FK, Nullable | Optional booking reference |
| redeemed_at | DateTime | Auto-set | Redemption timestamp |

## Relationships

- **user**: Many-to-one with [`User`](User.md) via backref `voucher_redemptions`
- **voucher**: Many-to-one with [`Voucher`](Voucher.md) via backref `redemption_logs` 

## Usage Examples
```python
# Log voucher redemption
log = VoucherRedemptionLog(
    user_id=123,
    voucher_id=456
)
db.session.add(log)

# Get user's redemption history
history = User.query.get(123).voucher_redemptions
```

## Business Rules
- Automatically timestamps redemptions
- Can optionally link to bookings
- Maintains audit trail of voucher usage