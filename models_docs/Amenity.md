# Amenity Model

## Description
Tracks amenities offered by vendors (e.g. WiFi, parking, food services).

## Fields

| Field | Type | Constraints | Description |
|-------|------|------------|-------------|  
| id | Integer | Primary Key | Unique identifier |
| vendor_id | Integer | FK, Not Null | Vendor offering amenity |
| name | String(50) | Not Null | Amenity name |
| available | Boolean | Default=False | Availability status |

## Relationships  

- **vendor**: Associated Vendor (many-to-one)

## Example Usage
```python
# Create new amenity  
amenity = Amenity(
    vendor_id=123,
    name="Free WiFi", 
    available=True
)

# Query amenities by vendor
amenities = Amenity.query.filter_by(vendor_id=123).all()