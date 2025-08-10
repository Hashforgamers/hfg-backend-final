# VendorPin Model

## Description
Stores security PIN codes for vendor authentication and verification.

## Fields

| Field | Type | Constraints | Description |
|-------|------|------------|-------------|
| id | Integer | Primary Key | Unique identifier |
| vendor_id | Integer | FK, Not Null | Vendor ID |
| pin_code | String(6) | Unique, Not Null | 6-digit security code |

## Relationships

- **vendor**: Associated Vendor (one-to-one)

## Security Features
- Used for additional authentication
- Separate from password
- Changed periodically for security

## Example Usage
```python
# Create a new vendor PIN
pin = VendorPin(
    vendor_id=123,
    pin_code="123456"
)

# Verify vendor PIN
is_valid = VendorPin.query.filter_by(
    vendor_id=123,
    pin_code=entered_pin
).first() is not None