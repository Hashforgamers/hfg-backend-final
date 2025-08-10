# ExtraServiceMenu Model

## Description
Represents individual menu items within extra service categories (e.g. specific food or drink items).

## Fields

| Field | Type | Constraints | Description |
|-------|------|------------|-------------|
| id | Integer | Primary Key | Unique identifier |
| category_id | Integer | FK, Not Null | Parent category ID |
| name | String(255) | Not Null | Item name |
| price | Float | Not Null | Item price |
| description | String(500) | Nullable | Item description |
| is_active | Boolean | Default=True | Whether item is active |

## Relationships  

- **category**: Parent ExtraServiceCategory record

## Example Usage
```python
# Create menu item
menu_item = ExtraServiceMenu(
    category_id=1,
    name="Coca-Cola",
    price=2.50,
    description="330ml can, chilled",
    is_active=True
)

# Get active menu items
items = ExtraServiceMenu.query.filter_by(
    category_id=1,
    is_active=True
).all()