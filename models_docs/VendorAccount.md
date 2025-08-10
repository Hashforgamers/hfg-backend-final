# VendorAccount Model

## Description
Manages vendor login/account credentials separately from business details.

## Fields

| Field | Type | Constraints | Description |
|-------|------|------------|-------------|
| id | Integer | Primary Key | Unique identifier |
| email | String(255) | Unique, Not Null | Account email |
| name | String(255) | Nullable | Account holder name |
| created_at | DateTime | Default=Current Time | Account creation date |

## Relationships  

- **vendors**: Associated Vendor records (one-to-many)

## Security Notes
- Credentials stored separately from business data
- Email serves as username
- Password managed through separate model

## Example Usage
```python
# Create vendor account 
account = VendorAccount(
    email="vendor@example.com",
    name="John Doe"
)

# Get account with vendors
account = VendorAccount.query.options(
    joinedload(VendorAccount.vendors)
).first()