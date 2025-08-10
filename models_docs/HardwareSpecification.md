# HardwareSpecification Model

## Description
Stores technical specifications for gaming console hardware configurations.

## Fields

| Field | Type | Constraints | Description |
|-------|------|------------|-------------|
| id | Integer | Primary Key | Unique identifier |
| processor_type | String(100) | Nullable | CPU/processor details |
| graphics_card | String(100) | Nullable | GPU details |
| ram_size | String(50) | Nullable | Memory capacity |
| storage_capacity | String(50) | Nullable | Storage specifications |
| connectivity | String(200) | Nullable | Network/connection options |
| console_model_type | String(200) | Nullable | Console variant details |
| console_id | Integer | FK, Not Null | Associated console |

## Relationships  

- **console**: Parent Console record (one-to-one)

## Example Usage
```python
# Create hardware specs
specs = HardwareSpecification(
    console_id=1,
    processor_type="Ryzen 7 5800X",
    graphics_card="RTX 3080",
    ram_size="16GB DDR4",
    storage_capacity="1TB NVMe SSD"
)

# Get specs for console
specs = HardwareSpecification.query.filter_by(console_id=1).first()