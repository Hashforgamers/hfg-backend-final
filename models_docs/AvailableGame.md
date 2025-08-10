# AvailableGame Model

## Description
Represents games available for booking from vendors.

## Fields

| Field | Type | Constraints | Description |
|-------|------|-------------|-------------|
| id | Integer | Primary Key | Unique game ID |
| vendor_id | Integer | FK, Not Null | Vendor providing the game |
| game_name | String(50) | Not Null | Name of game |
| total_slot | Integer | Not Null | Total available slots |
| single_slot_price | Integer | Not Null | Price per slot |

## Relationships

- **vendor**: Vendor providing game (many-to-one)
- **slots**: Associated time slots (one-to-many)
- **bookings**: Associated bookings (one-to-many)

## Methods

- **to_dict_for_booking()**: Serializes game data including vendor info

## Example Usage
```python
# Create available game
game = AvailableGame(
    vendor_id=1,
    game_name="Pinball Tournament",
    total_slot=10,
    single_slot_price=1500
)

# Get games with vendor info
games = AvailableGame.query.options(
    joinedload(AvailableGame.vendor)
).all()