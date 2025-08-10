# PriceAndCost Model

## Description
Manages pricing and cost information for console rentals/sales.

## Fields

| Field | Type | Constraints | Description |
|-------|------|------------|-------------|
| id | Integer | Primary Key | Unique identifier |
| price | Integer | Not Null | Retail purchase price |
| rental_price | Integer | Not Null | Hourly/daily rental rate |
| warranty_period | String(50) | Nullable | Warranty duration |
| insurance_status | String(50) | Not Null | Insurance coverage status |
| console_id | Integer | FK, Not Null | Associated console |

## Relationships  

- **console**: Parent Console record (one-to-one)

## Business Logic
- Used for both sales and rental scenarios
- Tracks warranty and insurance details
- Links to specific console configuration

## Example Usage
```python
# Set pricing for console
pricing = PriceAndCost(
    price=99900,
    rental_price=1500,
    warranty_period="1 year",
    insurance_status="included",
    console_id=1
)

# Get pricing info
pricing = PriceAndCost.query.filter_by(console_id=1).first()