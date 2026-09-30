# Test Plan

| Test | Expected result |
|---|---|
| Add valid product | Unique product ID and saved record |
| Negative price | Rejected by validation |
| Search product | Matching records displayed |
| Edit product | Product data updated |
| Delete product | Product removed after confirmation |
| Bill with enough stock | Bill saved and stock decreases |
| Bill over available stock | Item rejected |
| Udhaar without customer | Sale rejected |
| Add customer | Unique customer ID |
| Record payment | Pending amount decreases |
| Warranty record | Expiry calculated |
| Dashboard | Summary values displayed |
| JSON read/write | Data persists across runs |
