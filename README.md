# Wilmington Travel Agency

Wilmington Travel Agency is a full-stack modernization of my 2024 computer science capstone. The original submission was a three-page static travel website. This version preserves that work in `legacy/` and rebuilds the experience with a React and TypeScript interface, a Flask API, persistent data, validation and automated tests.

> **Project status:** v0.2.0 establishes the modern application foundation and first complete read workflow. Destination data is stored by the API, returned through a searchable endpoint and rendered by the responsive client. Authentication and booking remain planned work and are not represented as complete.

## Demonstrated skills

- Component-based React and TypeScript development
- REST API design with Flask
- Relational modeling with SQLAlchemy
- Server-side input validation and safe JSON error responses
- Responsive and accessible interface design
- Backend integration testing with pytest
- Environment-based configuration and containerization
- Incremental modernization of a legacy codebase

## Architecture

```text
Browser → React client → Flask REST API → SQLAlchemy → SQLite
```

The client requests destinations from `GET /api/destinations`. The API performs case-insensitive filtering and returns a stable JSON representation. Contact messages are validated server-side before persistence.

See [Architecture](docs/architecture.md), [API reference](docs/api.md), and [Security](docs/security.md) for the design decisions and current limitations.

## Run locally

### Backend

```bash
cd backend
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements-dev.txt
flask --app run:app run
```

### Frontend

In a second terminal:

```bash
cd frontend
npm install
npm run dev
```

Open `http://localhost:5173`. Vite proxies `/api` requests to the Flask server.

### Docker

```bash
docker compose up --build
```

Open `http://localhost:5173`.

## Test

```bash
cd backend
pytest
ruff check .
```

```bash
cd frontend
npm run build
```

## API summary

| Method | Endpoint | Purpose |
| --- | --- | --- |
| `GET` | `/api/health` | Service health and version |
| `GET` | `/api/destinations` | List destinations |
| `GET` | `/api/destinations?q=Berlin` | Filter by city or country |
| `POST` | `/api/contact` | Validate and store a contact request |

## Project history

The untouched college submission and its original description are retained in `legacy/`. It is intentionally not presented as a production application. See [Legacy assessment](docs/legacy-assessment.md) for the issues identified before modernization.

## Roadmap

- Destination detail pages and saved trips
- Secure registration, login and logout
- Role-based administration
- Booking-request workflow
- Database migrations and PostgreSQL deployment profile
- Frontend component tests and end-to-end tests
- Continuous integration and deployment

## License

Source code is available under the MIT License. Legacy photographs are retained for historical and educational context; their original licensing information was not included in the capstone archive and must be verified or replaced before public deployment.
