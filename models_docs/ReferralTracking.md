# ReferralTracking Model

## Description
Tracks user referrals and manages the referral reward program.

## Fields

| Field | Type | Constraints | Description |
|-------|------|------------|-------------|
| id | Integer | Primary Key | Unique identifier |
| referrer_code | String(10) | Nullable | Referral code used |
| referred_user_id | Integer | FK, Nullable | New user from referral |
| timestamp | DateTime | Default=Current Time | When referral occurred |

## Key Features
- Tracks successful conversions of referral codes
- Links referrers to their referred users
- Used to calculate referral bonuses

## Example Usage
```python
# Record new referral 
referral = ReferralTracking(
    referrer_code="REF123",
    referred_user_id=456
)

# Get user's referral history
history = ReferralTracking.query.filter_by(
    referrer_code="REF123"
).all()