# UserHashCoin Model  

## Description  
Tracks user cryptocurrency balances (HashCoins) with automatic timestamp updates.

## Fields  

| Field | Type | Constraints | Description |  
|-------|------|-------------|-------------|
| id | Integer | PK | Unique identifier |
| user_id | Integer | FK, Unique, Not Null | References users.id |
| hash_coins | Integer | Default=0 | Cryptocurrency balance |  
| updated_at | DateTime | Auto-update | Last balance update |

## Relationships  

- **user**: 1:1 with User model via backref `hash_coin_balance`

## Usage  

```python
# Check balance
balance = UserHashCoin.query.filter_by(user_id=123).first().hash_coins

# Update balance  
coin = UserHashCoin.query.filter_by(user_id=123).first()  
coin.hash_coins += 10  
db.session.commit()  
```  

## Business Logic  
- Auto-tracks last updated timestamp  
- Enforces single record per user (unique constraint)  
- Default zero balance for new users