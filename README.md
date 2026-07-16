<div align="center">

# 💳 Payment Reconciliation Service

### Production-ready backend service for payment lifecycle processing, reconciliation, and transaction management

<p align="center">

![Python](https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-0.116-009688?style=for-the-badge&logo=fastapi)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-16-336791?style=for-the-badge&logo=postgresql)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-2.x-D71F00?style=for-the-badge)
![Alembic](https://img.shields.io/badge/Alembic-Migrations-darkgreen?style=for-the-badge)
![Docker](https://img.shields.io/badge/Docker-Containerized-2496ED?style=for-the-badge&logo=docker)
![Pytest](https://img.shields.io/badge/Tested-Pytest-success?style=for-the-badge&logo=pytest)
![Render](https://img.shields.io/badge/Deployed-Render-46E3B7?style=for-the-badge&logo=render)

</p>

---

### 🚀 Solutions Engineer Take Home Assignment

*A production-minded payment reconciliation backend built using FastAPI, PostgreSQL, SQLAlchemy, Alembic and Docker.*

</div>

---

# 🌐 Live Demo

| Resource | Link |
|----------|------|
| **Live API** | https://payment-reconciliation-service-n4hn.onrender.com |
| **Swagger Documentation** | https://payment-reconciliation-service-n4hn.onrender.com/docs |
| **Health Endpoint** | https://payment-reconciliation-service-n4hn.onrender.com/health |
| **GitHub Repository** | https://github.com/Abhay-SKulkarni123/payment-reconciliation-service |
| **Postman Collection** | **<ADD_POSTMAN_LINK>** |
| **Demo Video** | **<ADD_LOOM_OR_YOUTUBE_LINK>** |

---

# 📖 Overview

This project implements a **production-ready Payment Reconciliation Service** capable of ingesting payment lifecycle events, maintaining transaction state, preserving event history, and exposing operational APIs for reconciliation reporting.

The system is designed with production engineering practices in mind, including:

- Idempotent event ingestion
- Transaction state management
- Event sourcing approach
- SQL-optimized querying
- Automatic database migrations
- Containerized deployment
- Public cloud deployment
- Comprehensive API documentation

---

# ✨ Features

- ✅ Idempotent payment event ingestion with duplicate detection
- ✅ Transaction management with filtering, pagination, and sorting
- ✅ Reconciliation summary and discrepancy detection
- ✅ Payment lifecycle validation using a state machine
- ✅ PostgreSQL + SQLAlchemy + Alembic
- ✅ Dockerized deployment with Docker Compose
- ✅ Automated API testing with Pytest
- ✅ Public deployment with interactive Swagger/OpenAPI documentation

---

# 📸 Project Preview

## Swagger Documentation

> Replace with screenshot before submission

```
docs/images/swagger.png
```

---

## Transaction APIs

> Replace with screenshot before submission

```
docs/images/transactions.png
```

---

## Reconciliation APIs

> Replace with screenshot before submission

```
docs/images/reconciliation.png
```

---

## Docker Deployment

> Replace with screenshot before submission

```
docs/images/docker.png
```

---

## Render Deployment

> Replace with screenshot before submission

```
docs/images/render.png
```

---

# 🏗 Architecture

```text
                         Client / Partner System
                                  │
                                  │ REST API
                                  ▼
                     ┌─────────────────────────┐
                     │       FastAPI App       │
                     └────────────┬────────────┘
                                  │
               ┌──────────────────┼──────────────────┐
               ▼                  ▼                  ▼
         Event Service      Transaction API    Reconciliation API
               │                  │                  │
               └──────────────────┼──────────────────┘
                                  ▼
                       Business Logic Layer
                                  │
                     Transaction State Machine
                                  │
                                  ▼
                          SQLAlchemy ORM
                                  │
                                  ▼
                           PostgreSQL Database
                                  │
                                  ▼
                           Alembic Migrations
```

---

# 🎯 Assignment Coverage

| Requirement | Status |
|-------------|--------|
| Event Ingestion | ✅ |
| Idempotency | ✅ |
| Transaction APIs | ✅ |
| Event History | ✅ |
| Reconciliation Summary | ✅ |
| Discrepancy Detection | ✅ |
| SQL Database | ✅ |
| 10,000+ Sample Events | ✅ |
| Docker Support | ✅ |
| Public Deployment | ✅ |
| Swagger Documentation | ✅ |
| Automated Tests | ✅ |

---

# 🛠 Technology Stack

| Category | Technology | Purpose |
|-----------|------------|---------|
| **Language** | Python 3.11 | Backend Development |
| **Framework** | FastAPI | REST API Framework |
| **Database** | PostgreSQL 16 | Relational Database |
| **ORM** | SQLAlchemy 2.x | Database ORM |
| **Migration Tool** | Alembic | Schema Versioning |
| **Validation** | Pydantic v2 | Request & Response Validation |
| **Testing** | Pytest | Automated Testing |
| **Containerization** | Docker & Docker Compose | Development & Deployment |
| **Deployment** | Render | Public Cloud Hosting |

---

# 📁 Project Structure

```text
payment-reconciliation-service/
│
├── alembic/                         # Database migrations
│   ├── versions/
│   └── env.py
│
├── app/
│   ├── models/                      # SQLAlchemy models
│   ├── routes/                      # API endpoints
│   ├── schemas/                     # Pydantic schemas
│   ├── services/                    # Business logic
│   ├── database.py                  # Database configuration
│   ├── crud.py                      # Database operations
│   ├── state_machine.py             # Payment lifecycle rules
│   ├── config.py                    # Environment configuration
│   └── main.py                      # FastAPI application
│
├── sample_data/
│   └── sample_events.json
│
├── tests/
│   ├── test_events.py
│   ├── test_transactions.py
│   └── test_reconciliation.py
│
├── Dockerfile
├── docker-compose.yml
├── start.sh
├── requirements.txt
├── alembic.ini
├── .env.example
└── README.md
```

---

# 🏛 Engineering Decisions

This project was designed with a focus on simplicity, maintainability, and production-readiness while staying within the scope of the assignment.



The following design decisions were made to keep the service simple, maintainable, and production-ready:

- **Layered Architecture** — Separated routes, services, CRUD, and models for clear separation of concerns.
- **State Machine Validation** — Enforces valid payment lifecycle transitions and prevents invalid state updates.
- **Idempotent Event Processing** — Duplicate events are ignored using a unique `event_id`, ensuring safe retries.
- **Event History Preservation** — Every payment event is stored to provide a complete audit trail.
- **Normalized Database Schema** — Separate merchant, transaction, and event tables minimize redundancy and simplify queries.
- **SQL-first Querying** — Filtering, pagination, sorting, and reconciliation aggregations are performed directly in PostgreSQL.
- **Automated Database Migrations** — Alembic manages schema versioning across environments.
- **Containerized Deployment** — Docker and Docker Compose provide consistent local and cloud environments.

---

## Layered Architecture

The application follows a layered architecture to keep responsibilities well separated.

```text
                API Routes
                    │
                    ▼
             Service Layer
                    │
                    ▼
            CRUD / Repository
                    │
                    ▼
              PostgreSQL Database
```

### Benefits

- Clear separation of concerns
- Easier unit testing
- Better maintainability
- Reusable business logic
- Simplified API layer

---

# 🔄 State Machine Validation

Incoming events are validated before updating a transaction.

This prevents invalid lifecycle transitions such as:

❌ Settled → Payment Initiated

❌ Failed → Processed

❌ Settled → Failed

Only valid transitions are allowed to update transaction state.

---

# 🔒 Idempotency

A key assignment requirement was ensuring duplicate events do not corrupt state.

Implementation:

- Every event contains a unique **event_id**
- Duplicate event IDs are detected before processing
- Existing transaction state remains unchanged
- Event history remains consistent

This guarantees safe retries from external systems.

---

# 🧪 Testing Strategy

The project includes automated API tests covering the primary workflows.

### Tested Scenarios

- Event ingestion
- Duplicate event handling
- Transaction retrieval
- Transaction filtering
- Reconciliation summary
- Reconciliation discrepancies
- Health endpoint

Run all tests:

```bash
pytest
```

Expected result:

```text
=========================
7 passed
=========================
```

---

# 👨‍💻 Author

**Abhay S. Kulkarni**

Solutions Engineer Take-Home Assignment

GitHub: https://github.com/Abhay-SKulkarni123

LinkedIn: https://www.linkedin.com/in/abhaysk040304/

Portfolio : https://portfolio-wheat-ten-27.vercel.app/

Email : abhayskulkarni11@gmail.com

Phone : +91 9353656880

---

<div align="center">

### ⭐ Thank you for taking the time to review this submission.

Built with FastAPI, PostgreSQL, SQLAlchemy, Alembic, Docker, and Render.

</div>