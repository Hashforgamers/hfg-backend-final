# Game Model

## Description
Represents game titles that can be supported by vendors. Acts as a reference/master list of all possible games.

## Fields

| Field | Type | Constraints | Description |
|-------|------|------------|-------------|
| id | Integer | Primary Key | Unique identifier |
| name | String(255) | Unique, Not Null | Game title/name |

## Relationships  

- **supported_by**: Associated SupportedGame records (one-to-many)

## Example Usage
```python
# Create new game
game = Game(
    name="Call of Duty: Modern Warfare"
)

# Get all supported games
games = Game.query.options(
    joinedload(Game.supported_by)
).all()