# ExtraServiceCategory Model

## Description
Represents categories for extra services that can be offered by vendors (e.g. food, drinks, merchandise).

## Fields

| Field | Type | Constraints | Description |
|-------|------|------------|-------------|
| id | Integer | Primary Key | Unique identifier |
| vendor_id | Integer | FK, Not Null | Vendor offering the service category |
| name | String(255) | Not Null | Category name (e.g. "Food & Beverage") |
| description | String(500) | Nullable | Category description |
| is_active | Boolean | Default=True | Whether category is active |

## Relationships  

- **vendor**: Associated Vendor record (many-to-one)
- **menus**: ExtraServiceMenu items in this category (one-to-many)

## Example Usage
```python
# Create new service category
category = ExtraServiceCategory(
    vendor_id=123,
    name="Drinks",
    description="Alcoholic and non-alcoholic beverages",
    is_active=True
)

# Get active categories for vendor
categories = ExtraServiceCategory.query.filter_by(
    vendor_id=123, 
    is_active=True
).all()