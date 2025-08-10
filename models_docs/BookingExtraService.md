# BookingExtraService Model

## Description
Tracks additional services added to bookings (food, drinks, etc.).

## Fields

| Field | Type | Constraints | Description |
|-------|------|------------|-------------|
| id | Integer | Primary Key | Unique identifier |
| booking_id | Integer | FK, Not Null | Associated booking |
| menu_item_id | Integer | FK, Not Null | Service menu item |
| quantity | Integer | Default=1, Not Null | Quantity ordered |
| unit_price | Float | Not Null | Price per unit |
| total_price | Float | Not Null | Calculated total price |

## Relationships

- **booking**: Parent Booking record (many-to-one)
- **menu_item**: ExtraServiceMenu item (many-to-one)

## Example Usage
```python
# Add extra service to booking
extra_service = BookingExtraService(
    booking_id=123,
    menu_item_id=456,
    quantity=2,
    unit_price=10.50,
    total_price=21.00
)