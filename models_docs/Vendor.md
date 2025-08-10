# Vendor Model

## Description
Represents gaming cafe vendors that provide services on the platform. Central entity with relationships to most other models.

## Fields

| Field | Type | Constraints | Description |
|-------|------|------------|-------------|
| id | Integer | Sequence, PK | Unique vendor ID (starts from 2000) |
| cafe_name | String(255) | Not Null | Business name |
| owner_name | String(255) | Not Null | Owner's name |
| description | String(255) | Nullable | Business description |
| business_registration_id | Integer | FK, Nullable | Business registration |
| timing_id | Integer | FK, Nullable | Operating hours ID |
| account_id | Integer | FK, Nullable | Associated vendor account |
| created_at | DateTime | Default=Current Time | Registration date |
| updated_at | DateTime | Default=Current Time | Last update timestamp |

## Relationships

- **physical_address**: Business location (one-to-one)
- **contact_info**: Contact details (one-to-one)  
- **business_registration**: Legal registration (one-to-one)
- **timing**: Operating hours (one-to-one)
- **amenities**: Offered amenities (one-to-many)
- **documents_submitted**: Submitted docs (one-to-many)
- **opening_days**: Opening schedule (one-to-many)
- **available_games**: Offered games (one-to-many)
- **account**: Vendor account (one-to-one) 
- **pin**: Security pin (one-to-one)
- **password**: Password (one-to-one)
- **supported_games**: Supported games (one-to-many)
- **extra_service_categories**: Extra services (one-to-many)
- **statuses**: Status history (one-to-many)
- **transactions**: Payments (one-to-many)

## Example Usage
```python
# Create new vendor
vendor = Vendor(
    cafe_name="Gamer's Hub",
    owner_name="John Doe",
    description="Premium esports gaming center"
)

# Query vendor with relationships
vendor = Vendor.query.options(
    joinedload(Vendor.contact_info),
    joinedload(Vendor.physical_address)
).first()