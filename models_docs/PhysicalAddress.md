# PhysicalAddress Model

## Description
Stores physical address information that can be attached to various entities (polymorphic relationship).

## Fields

| Field | Type | Constraints | Description |
|-------|------|------------|-------------|
| id | Integer | Primary Key | Unique identifier |
| address_type | String(50) | Not Null | Type of address (home/business/etc) |
| addressLine1 | String(255) | Not Null | Primary address line |
| addressLine2 | String(255) | Nullable | Secondary address line |
| pincode | String(10) | Not Null | Postal/ZIP code |
| state | String(100) | Not Null | State/Province |
| country | String(100) | Not Null | Country |
| is_active | Boolean | Default=True | Whether address is active |
| latitude | String(20) | Nullable | GPS coordinates |
| longitude | String(20) | Nullable | GPS coordinates |
| parent_id | Integer | Not Null | Associated entity ID |
| parent_type | String(50) | Not Null | Entity type (user/vendor/etc) |

## Relationships
Polymorphic relationship with parent entities (user, vendor, etc)

## Example Usage
```python 
# Create address for a vendor
address = PhysicalAddress(
    address_type="business",
    addressLine1="123 Gaming St",
    pincode="10001",
    state="New York",
    country="USA",
    parent_id=123,
    parent_type="vendor"
)

# Get all active vendor addresses  
addresses = PhysicalAddress.query.filter_by(
    parent_type="vendor",
    is_active=True
).all()