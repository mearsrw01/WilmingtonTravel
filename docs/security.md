# Security Design

## Implemented controls

- The API accepts and returns JSON rather than rendering user-provided HTML.
- SQLAlchemy produces parameterized queries for destination search.
- Contact fields are normalized, length-limited and validated on the server.
- Error responses do not expose stack traces or database details.
- CORS is restricted to the configured front-end origin.
- Responses include anti-sniffing, anti-framing, referrer and content-security headers.
- Secrets and database locations are configured through environment variables.
- The local database and environment files are excluded from version control.

## Trust boundaries

Browser input is untrusted. Client-side limits improve usability but are not security controls; the API repeats all validation before persistence. The database is accessed only through SQLAlchemy models.

## Current limitations

- The contact endpoint is not yet rate-limited.
- Authentication and authorization are not implemented.
- SQLite is intended for local demonstration rather than concurrent production traffic.
- The prototype does not process payments or store payment-card data.
- A production deployment would require HTTPS, centralized logging, managed secrets, database migrations and monitoring.

## Planned threat-model expansion

Identity and booking features will receive a data-flow diagram and STRIDE review before implementation. Tests will cover broken access control, session handling, input abuse and sensitive-data exposure.

