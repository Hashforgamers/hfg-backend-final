# Console Model

## Description
Represents physical gaming console units available at vendors.

## Fields

| Field | Type | Constraints | Description |
|-------|------|------------|-------------|  
| id | Integer | Primary Key | Unique identifier |
| console_number | Integer | Not Null | Console identifier number |
| model_number | String(50) | Not Null | Manufacturer model number |
| serial_number | String(100) | Not Null | Unit serial number |
| brand | String(50) | Not Null | Manufacturer brand |
| console_type | String(50) | Not Null | Console type/generation |
| release_date | Date | Not Null | Original release date |
| description | String(500) | Nullable | Additional description |

## Relationships  

- **hardware_specifications**: Associated HardwareSpecification (one-to-one)
- **maintenance_status**: Associated MaintenanceStatus (one-to-one)  
- **price_and_cost**: Associated PriceAndCost (one-to-one)
- **additional_details**: Associated AdditionalDetails (one-to-one)
- **available_games**: Associated AvailableGame records (many-to-many)

## Example Usage
```python
# Create new console
console = Console(
    console_number=101,
    model_number="PS5-1001",
    serial_number="PS5A123456789",
    brand="Sony",
    console_type="PlayStation 5",
    release_date="2020-11-12",
    description="Standard edition with 825GB SSD"
)

# Query consoles with games
consoles = Console.query.options(
    joinedload(Console.available_games)
).filter_by(brand="Sony").all()