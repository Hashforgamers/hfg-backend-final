# HashWallet Model

## Description
Stores user balances for the platform's cryptocurrency (HashCoins). Each user has exactly one wallet.

## Fields

| Field | Type | Constraints | Description |
|-------|------|------------|-------------|
| id | Integer | Primary Key | Unique identifier |
| user_id | Integer | FK, Unique, Not Null | Wallet owner |
| balance | Integer | Default=0 | Current HashCoin balance |

## Relationships

- **user**: Associated User record (one-to-one)

## Key Features
- Enforced 1:1 relationship with users (via unique constraint)
- Balance can be positive or negative (for debt scenarios)

## Example Usage
```python
# Get or create wallet
wallet = HashWallet.query.filter_by(user_id=123).first() or HashWallet(user_id=123)

# Update balance 
wallet.balance += 1000  # Add coins
db.session.commit()

# Check balance
balance = HashWallet.query.filter_by(user_id=123).first().balance