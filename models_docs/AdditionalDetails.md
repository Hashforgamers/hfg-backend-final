# AdditionalDetails Model

## Description
Stores supplemental information about game consoles and their configurations.

## Fields

| Field | Type | Constraints | Description |
|-------|------|------------|-------------|  
| id | Integer | Primary Key | Unique identifier |
| supported_games | String(500) | Nullable | Supported game titles |
| accessories | String(500) | Nullable | Available accessories |
| console_id | Integer | FK, Not Null | Associated console |

## Relationships  

- **console**: Parent Console (many-to-one)

## Example Usage
```python
# Create additional details
details = AdditionalDetails(
    console_id=1,
    supported_games="Game1, Game2, Game3",
    accessories="Controllers, Headsets"
)

# Query by console
details = AdditionalDetails.query.filter_by(console_id=1).first()