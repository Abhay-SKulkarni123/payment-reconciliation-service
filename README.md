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

# ⚡ Highlights

- Public deployment on Render
- Interactive Swagger/OpenAPI documentation
- Dockerized application
- 10,355 sample payment events
- Fully automated database migrations
- 7 automated tests passing

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

```
<p align="center">
  <img src="docs/images/swagger.png" width="95%" alt="Swagger UI"/>
</p>

```

---

## Transaction APIs

```
<p align="center">
  <img src="docs/images/transactions.png" width="95%" alt="Swagger UI"/>
</p>
```

---

## Reconciliation APIs

```
<p align="center">
  <img src="docs/images/reconciliation.png" width="95%" alt="Swagger UI"/>
</p>

```

---

## Docker Deployment

```
<p align="center">
  <img src="docs/images/docker.png" width="95%" alt="Swagger UI"/>
</p>
```

---

## Render Deployment

```
<p align="center">
  <img src="docs/images/render.png" width="95%" alt="Swagger UI"/>
</p>
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

# 🏛 Engineering Decisions

The project emphasizes simplicity, maintainability, and production-readiness through the following design decisions:

- **Layered Architecture** — Separates routes, services, CRUD, and models for clear separation of concerns.
- **State Machine Validation** — Ensures only valid payment lifecycle transitions are accepted.
- **Idempotent Event Processing** — Prevents duplicate event processing using a unique `event_id`.
- **Event History Preservation** — Stores every event to maintain a complete audit trail.
- **Normalized Database Design** — Separates merchants, transactions, and payment events for efficient querying.
- **SQL-first Querying** — Filtering, pagination, sorting, and reconciliation are executed directly in PostgreSQL.
- **Alembic Migrations** — Provides version-controlled schema management.
- **Dockerized Deployment** — Ensures consistent local and cloud environments.

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