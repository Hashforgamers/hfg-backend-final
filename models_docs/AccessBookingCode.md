# AccessBookingCode Model

## Description
Manages unique access codes used for booking verification.

## Fields

| Field | Type | Constraints | Description |
|-------|------|------------|-------------|
| id | Integer | Primary Key | Unique identifier |
| access_code | String(6) | Unique, Not Null | 6-digit access code |
| created_at | DateTime | Default=Current Time | Creation timestamp |

## Relationships

- **bookings**: Associated Booking records (one-to-many)

## Example Usage
```python
# Create new access code
new_code = AccessBookingCode(access_code='ABC123')

# Get codes with bookings
codes = AccessBookingCode.query.options(
    joinedload(AccessBookingCode.bookings)
).all()