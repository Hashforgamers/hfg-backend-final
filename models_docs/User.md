# User Model

## Description
Represents platform users with gaming profiles and authentication.

## Fields

| Field | Type | Constraints | Description |
|-------|------|------------|-------------|
| id | Integer | Sequence, PK | User ID (starts from 2000) |
| fid | String(255) | Unique, Not Null | Firebase auth ID |
| avatar_path | String(255) | Nullable | Profile picture path |
| name | String(255) | Not Null | Full name |
| gender | String(50) | Nullable | Gender |
| dob | Date | Nullable | Date of birth |
| game_username | String(255) | Unique, Not Null | In-game username |
| referral_code | String(10) | Unique | Referral identifier |
| referred_by | String(10) | FK | Referrer's code |
| referral_rewards | Integer | Default=0 | Earned credits |
| parent_type | String(50) | Not Null | Default='user' |

## Relationships  

- **fcm_tokens**: Push notification tokens (one-to-many)
- **physical_address**: User address (one-to-one)
- **contact_info**: Contact details (one-to-one)
- **password**: Auth credentials (one-to-one)

## Usage Examples
```python
# Create new user
user = User(
    fid="firebase_id_123",
    name="Game Player",
    game_username="gamer123"
)

# Get user with relationships
user = User.query.options(
    joinedload(User.contact_info),
    joinedload(User.physical_address)
).filter_by(id=123).first()