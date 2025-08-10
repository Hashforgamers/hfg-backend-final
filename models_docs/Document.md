# Document Model

## Description  
Stores documents submitted by vendors (e.g. business licenses, certifications).

## Fields  

| Field | Type | Constraints | Description |  
|-------|------|------------|-------------|  
| id | Integer | Primary Key | Unique identifier |
| vendor_id | Integer | FK, Not Null | Vendor who submitted document |
| document_type | String(100) | Not Null | Type of document |
| file_path | String(255) | Not Null | Storage path/URL for document |  
| uploaded_at | DateTime | Default=Current Time | When document was uploaded |
| status | String(20) | Default='unverified' | Verification status |

## Relationships

- **vendor**: Associated Vendor record (many-to-one)

## Example Usage  
```python
# Create new document
doc = Document(
    vendor_id=123,
    document_type="Business License",
    file_path="https://drive.google.com/doc123",
    status="pending_review"
)

# Get unverified documents  
docs = Document.query.filter_by(status="unverified").all()