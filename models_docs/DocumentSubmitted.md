# DocumentSubmitted Model

## Description
Tracks which documents have been submitted by vendors for verification.

## Fields  

| Field | Type | Constraints | Description |
|-------|------|------------|-------------|
| id | Integer | Primary Key | Unique identifier |
| vendor_id | Integer | FK, Not Null | Vendor who submitted the document |
| document_name | String(50) | Not Null | Name/type of document |
| submitted | Boolean | Default=False | Submission status |

## Relationships

- **vendor**: Associated Vendor record (many-to-one)

## Example Usage
```python
# Mark document as submitted
doc = DocumentSubmitted(
    vendor_id=123,
    document_name="Business License",
    submitted=True
)

# Get pending submissions
pending = DocumentSubmitted.query.filter_by(
    submitted=False
).all()