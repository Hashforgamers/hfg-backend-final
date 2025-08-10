# Voucher Model

## Description
Handles discount vouchers/coupons assigned to users.

## Fields

| Field | Type | Constraints | Description |
|-------|------|-------------|-------------|
| id | Integer | PK | Voucher ID |
| code | String(20) | Unique, Not Null | Voucher code |
| user_id | Integer | FK, Not Null | Associated user |
| discount_percentage | Integer | Default=100 | Discount amount (0-100) |
| is_active | Boolean | Default=True | Active status |
| created_at | DateTime | Auto-set | Creation timestamp |

## Relationships

- **user**: Many-to-one with [`User`](User.md) via backref `vouchers`

## Usage Examples
```python
# Create new voucher
voucher = Voucher(
    code="WELCOME10", 
    user_id=123,
    discount_percentage=10
)

# Get active vouchers
active_vouchers = Voucher.query.filter_by(
    user_id=123, 
    is_active=True
).all()
```

## Business Rules
- Codes must be unique
- Auto-tracks creation time
- Defaults to 100% discount if not specified