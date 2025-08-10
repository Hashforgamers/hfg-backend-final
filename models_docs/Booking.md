# Booking Model

## Description
Tracks user bookings for game sessions and associated data.

## Fields

| Field | Type | Constraints | Description |
|-------|------|-------------|-------------|
| id | Integer | Primary Key | Unique booking ID |
| user_id | Integer | Not Null | ID of booking user |
| game_id | Integer | FK, Not Null | Reference to AvailableGame |
| slot_id | Integer | FK, Not Null | Reference to Slot |
| status | String(20) | Default='pending_verified' | Booking status |
| access_code_id | Integer | FK, Nullable | Reference to access code |

## Relationships

- **game**: Associated AvailableGame (many-to-one)
- **slot**: Associated Slot (many-to-one) 
- **transaction**: Associated payment Transaction (one-to-one)
- **booking_extra_services**: Associated extra services (one-to-many)
- **access_code_entry**: Associated AccessBookingCode (many-to-one)

## Methods

- **to_dict()**: Serializes booking data including related objects
- **__repr__()**: Provides string representation

## Example Usage
```python
# Create booking
booking = Booking(
    user_id=123,
    game_id=456,
    slot_id=789,
    status='confirmed'
)

# Query with relationships
booking = Booking.query.options(
    joinedload(Booking.game),
    joinedload(Booking.slot)
).first()