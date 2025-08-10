# ContactInfo Model

## Description
Stores contact information that can be shared between both users and vendors (polymorphic relationship).

## Fields

| Field | Type | Constraints | Description |
|-------|------|------------|-------------|  
| id | Integer | Primary Key | Unique identifier |
| email | String(255) | Not Null | Contact email address |
| phone | String(50) | Not Null | Phone number |
| parent_id | Integer | Not Null | Associated parent record ID |
| parent_type | String(50) | Not Null | Parent type ('user' or 'vendor') |

## Relationships  

- **user**: Associated User record (when parent_type='user')
- **vendor**: Associated Vendor record (when parent_type='vendor')

## Special Features
- Uses SQLAlchemy polymorphic pattern for multiple parent types
- Single table inheritance (__mapper_args__)

## Example Usage
```python
# Create user contact info
user_contact = ContactInfo(
    email="user@example.com",
    phone="+1234567890",
    parent_id=user.id,
    parent_type='user'
)

# Get vendor contact info
vendor_contact = ContactInfo.query.filter_by(
    parent_id=vendor.id,
    parent_type='vendor'
).first()