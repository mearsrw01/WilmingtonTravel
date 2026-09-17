# Architecture

## Purpose

The modernization separates presentation, application behavior and persistence so each layer can change and be tested independently.

## Components

| Component | Responsibility |
| --- | --- |
| React client | Accessible interface, query state and API presentation |
| Flask API | Request validation, response contracts and application rules |
| SQLAlchemy | Relational models and database access |
| SQLite | Zero-configuration local persistence |
| Nginx | Production-style static serving and API proxying in Docker |

## Destination read flow

1. The user submits a city or country search.
2. The client URL-encodes the query and requests `/api/destinations`.
3. The API limits the query length and performs parameterized filtering through SQLAlchemy.
4. The API returns a JSON collection.
5. React renders results, an empty state or an error state.

## Boundaries

This release does not implement authentication, payments, ticket issuance or confirmed bookings. Future features will be added only with associated tests and documentation.

