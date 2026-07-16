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

# ⚙️ Getting Started

## Prerequisites

Ensure the following tools are installed before running the project locally.

| Software | Version |
|-----------|---------|
| Python | 3.11+ |
| PostgreSQL | 16+ |
| Docker *(Optional)* | Latest |
| Docker Compose *(Optional)* | Latest |
| Git | Latest |

---

# 🚀 Quick Start

Clone the repository.

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd payment-reconciliation-service
```

Create a virtual environment.

```bash
python -m venv .venv
```

Activate it.

### Windows

```bash
.venv\Scripts\activate
```

### Linux / macOS

```bash
source .venv/bin/activate
```

Install project dependencies.

```bash
pip install -r requirements.txt
```

---

# 🔐 Environment Variables

Create a `.env` file in the project root.

You can copy the provided example.

```bash
cp .env.example .env
```

Configure the following variables.

```env
DATABASE_URL=postgresql://postgres:<PASSWORD>@localhost:5432/payment_db

APP_NAME=Payment Reconciliation Service

APP_VERSION=1.0.0
```

---

# 🗄 Database Setup

Start PostgreSQL.

Create the database.

```sql
CREATE DATABASE payment_db;
```

Apply database migrations.

```bash
alembic upgrade head
```

The following tables will be created automatically.

- merchants
- transactions
- payment_events
- alembic_version

---

# ▶️ Running the Application

Start the FastAPI server.

```bash
uvicorn app.main:app --reload
```

Application

```
http://localhost:8000
```

Swagger Documentation

```
http://localhost:8000/docs
```

Health Endpoint

```
http://localhost:8000/health
```

---

# 🐳 Running with Docker

The project includes complete Docker support.

Build and start the containers.

```bash
docker compose up --build
```

Run in detached mode.

```bash
docker compose up -d
```

Stop the application.

```bash
docker compose down
```

The Docker setup automatically:

- Starts PostgreSQL
- Creates persistent database volume
- Runs Alembic migrations
- Starts FastAPI
- Exposes the API

Swagger

```
http://localhost:8001/docs
```

---

# 🧪 Running Tests

Execute the complete test suite.

```bash
pytest
```

Expected output

```text
============================= test session starts =============================

tests/test_events.py ........
tests/test_transactions.py ...
tests/test_reconciliation.py ..

============================== 7 passed ==============================
```

---

# 1️⃣ Ingest Payment Event

### Endpoint

```http
POST /events
```

Registers a payment lifecycle event and updates the corresponding transaction.

### Supported Event Types

| Event |
|--------|
| payment_initiated |
| payment_processed |
| payment_failed |
| settled |

### Example Request

```json
{
    "event_id": "render-test-001",
    "event_type": "payment_initiated",
    "transaction_id": "txn-render-001",
    "merchant_id": "merchant_render",
    "merchant_name": "Render Test Merchant",
    "amount": 999.99,
    "currency": "INR",
    "timestamp": "2026-01-08T12:11:58Z"
}
```

# 2️⃣ List Transactions

### Endpoint

```http
GET /transactions
```

Returns paginated transaction records.

### Supported Query Parameters

| Parameter | Description |
|------------|-------------|
| merchant_id | Filter by merchant |
| payment_status | Filter by payment status |
| start_date | Filter by start date |
| end_date | Filter by end date |
| page | Pagination |
| page_size | Page size |
| sort_by | Sorting column |
| sort_order | asc / desc |

### Example

```http
GET /transactions?merchant_id=merchant_1&page=1&page_size=20
```
---

# 🔄 Transaction State Management

Incoming events are validated through a state machine before updating the transaction.

Valid lifecycle:

```text
payment_initiated
        │
        ▼
payment_processed
        │
        ▼
     settled
```

Failure path:

```text
payment_initiated
        │
        ▼
payment_failed
```

Invalid transitions are rejected while preserving the existing transaction state.

---

# 📮 Postman Collection

A ready-to-use Postman collection containing all API endpoints is included with this repository.

**Import the collection and update the base URL to either:**

Local

```
http://localhost:8000
```

Production

```
https://payment-reconciliation-service-n4hn.onrender.com
```

---

# 🏛 Engineering Decisions

This project was designed with a focus on simplicity, maintainability, and production-readiness while staying within the scope of the assignment.

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

# 📈 Sample Dataset

To evaluate performance and reconciliation logic, the project includes a realistic dataset.

### Dataset Summary

| Metric | Value |
|---------|------:|
| Total Events | 10,355 |
| Merchants | 5 |
| Successful Payments | ✓ |
| Failed Payments | ✓ |
| Duplicate Events | ✓ |
| Pending Settlements | ✓ |
| Reconciliation Issues | ✓ |

The dataset can be loaded using:

```bash
python -m app.cli.load_sample_data
```

---

# 📮 Postman Collection

The repository includes a ready-to-use Postman collection covering every endpoint.

Import the collection and configure the base URL as:

**Production**

```
https://payment-reconciliation-service-n4hn.onrender.com
```

or

**Local**

```
http://localhost:8000
```

---

# 👨‍💻 Author

**Abhay S. Kulkarni**

Solutions Engineer Take-Home Assignment

GitHub: **<ADD_GITHUB_PROFILE>**

LinkedIn: **<ADD_LINKEDIN_PROFILE>**

---

<div align="center">

### ⭐ Thank you for reviewing this project!

If you have any questions or feedback, feel free to reach out.

Built with ❤️ using FastAPI, PostgreSQL, SQLAlchemy, Alembic, Docker, and Render.

</div>