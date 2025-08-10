# FcmToken Model

## Description
Stores Firebase Cloud Messaging (FCM) tokens for mobile push notifications.

## Fields

| Field | Type | Constraints | Description |
|-------|------|------------|-------------|
| id | Integer | Primary Key | Unique identifier |
| user_id | Integer | FK, Not Null | Associated user ID |
| token | String(512) | Unique, Not Null | FCM device token |
| platform | String(20) | Nullable | Device platform (iOS/Android) |
| created_at | DateTime | Default=Current Time | When token was registered |

## Relationships  

- **user**: Associated User record (many-to-one)

## Example Usage
```python
# Register new FCM token
fcm_token = FcmToken(
    user_id=123,
    token="sdflkj234...",
    platform="iOS",
)

# Get user's tokens 
tokens = FcmToken.query.filter_by(user_id=123).all()