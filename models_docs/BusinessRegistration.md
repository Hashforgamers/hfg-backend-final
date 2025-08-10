# BusinessRegistration Model

## Description
Stores business registration details for vendor entities.

## Fields

| Field | Type | Constraints | Description |
|-------|------|------------|-------------|  
| id | Integer | Primary Key | Unique identifier |
| registration_number | String(100) | Not Null | Official registration number |
| registration_date | Date | Not Null | Date of registration |

## Relationships  

- **vendors**: Associated Vendor records (one-to-many)

## Example Usage
```python
# Create business registration
reg = BusinessRegistration(
    registration_number="ABC12345", 
    registration_date="2023-01-15"
)

# Get all registered businesses
businesses = BusinessRegistration.query.all()