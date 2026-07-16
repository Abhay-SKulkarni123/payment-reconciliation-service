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

### Payment Processing

- ✅ Idempotent payment event ingestion
- ✅ Duplicate event detection
- ✅ Payment lifecycle state management
- ✅ Event history preservation
- ✅ Merchant normalization

---

### Transaction APIs

- ✅ Transaction listing
- ✅ Merchant filtering
- ✅ Payment status filtering
- ✅ Date range filtering
- ✅ Pagination
- ✅ Sorting
- ✅ Detailed transaction history

---

### Reconciliation

- ✅ Merchant reconciliation summary
- ✅ Settlement status tracking
- ✅ Reconciliation discrepancy detection
- ✅ Invalid state transition detection

---

### Engineering

- ✅ PostgreSQL database
- ✅ SQLAlchemy ORM
- ✅ Alembic migrations
- ✅ Docker support
- ✅ Docker Compose
- ✅ Automated tests
- ✅ Public Render deployment
- ✅ Swagger / OpenAPI documentation

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

# 🗄 Database Design

The database is normalized into three primary entities.

```text
                    ┌────────────────────┐
                    │     merchants      │
                    ├────────────────────┤
                    │ merchant_id (PK)   │
                    │ merchant_name      │
                    └─────────┬──────────┘
                              │ 1
                              │
                              │ N
                    ┌─────────▼──────────┐
                    │    transactions    │
                    ├────────────────────┤
                    │ id (PK)            │
                    │ transaction_id     │
                    │ merchant_id (FK)   │
                    │ amount             │
                    │ currency           │
                    │ payment_status     │
                    │ settlement_status  │
                    │ created_at         │
                    │ updated_at         │
                    └─────────┬──────────┘
                              │ 1
                              │
                              │ N
                    ┌─────────▼──────────┐
                    │   payment_events   │
                    ├────────────────────┤
                    │ event_id (PK)      │
                    │ transaction_id(FK) │
                    │ event_type         │
                    │ timestamp          │
                    │ raw_payload        │
                    └────────────────────┘
```

---

# 🔄 Payment Lifecycle State Machine

The service validates all incoming events using a state machine to prevent invalid transaction transitions.

```text
                    payment_initiated
                             │
                             ▼
                    payment_processed
                       │            │
                       │            ▼
                       │     payment_failed
                       │
                       ▼
                     settled
```

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

# ☁️ Public Deployment

The application is deployed on **Render**.

| Resource | URL |
|----------|-----|
| Live API | https://payment-reconciliation-service-n4hn.onrender.com |
| Swagger | https://payment-reconciliation-service-n4hn.onrender.com/docs |
| Health Check | https://payment-reconciliation-service-n4hn.onrender.com/health |

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

# 📊 Loading Sample Dataset

The repository includes a realistic payment event dataset containing **10,355 payment events** across multiple merchants.

Load the dataset.

```bash
python -m app.cli.load_sample_data
```

Expected output

```text
Processed 500 events...
Processed 1000 events...
...

Loaded 10355 events successfully.
```

---

# ❤️ Health Check

Verify the service is running.

```http
GET /health
```

Expected response

```json
{
    "status": "healthy",
    "database": "connected"
}
```

---

# 📡 API Documentation

The service exposes RESTful APIs for payment event ingestion, transaction retrieval, and reconciliation reporting.

Interactive OpenAPI documentation is available at:

**Local**

```
http://localhost:8000/docs
```

**Production**

```
https://payment-reconciliation-service-n4hn.onrender.com/docs
```

---

# API Overview

| Method | Endpoint | Description |
|----------|-----------|-------------|
| POST | `/events` | Ingest a payment lifecycle event |
| GET | `/transactions` | List transactions with filtering, pagination and sorting |
| GET | `/transactions/{transaction_id}` | Retrieve a transaction with complete event history |
| GET | `/reconciliation/summary` | Merchant reconciliation summary |
| GET | `/reconciliation/discrepancies` | Detect reconciliation inconsistencies |
| GET | `/health` | Application health check |
| GET | `/` | Service information |

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

### Example Response

```json
{
    "success": true,
    "message": "Event processed successfully.",
    "transaction_id": "txn-render-001"
}
```

---

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

### Example Response

```json
{
    "total": 773,
    "page": 1,
    "page_size": 20,
    "items": [
        {
            "transaction_id": "...",
            "merchant": {
                "merchant_id": "merchant_1",
                "merchant_name": "FreshBasket"
            },
            "amount": "22009.59",
            "currency": "INR",
            "payment_status": "payment_processed",
            "settlement_status": "settled"
        }
    ]
}
```

---

# 3️⃣ Transaction Details

### Endpoint

```http
GET /transactions/{transaction_id}
```

Returns the complete transaction information including its event history.

### Example

```http
GET /transactions/txn-render-001
```

### Response Includes

- Transaction metadata
- Merchant details
- Amount and currency
- Payment status
- Settlement status
- Created & updated timestamps
- Complete event history

---

# 4️⃣ Reconciliation Summary

### Endpoint

```http
GET /reconciliation/summary
```

Provides aggregated reconciliation statistics grouped by merchant.

### Example Response

```json
{
    "items": [
        {
            "merchant_id": "merchant_1",
            "merchant_name": "FreshBasket",
            "total_transactions": 773,
            "processed": 581,
            "failed": 151,
            "settled": 511,
            "pending_settlement": 262
        }
    ]
}
```

---

# 5️⃣ Reconciliation Discrepancies

### Endpoint

```http
GET /reconciliation/discrepancies
```

Returns transactions with inconsistent payment and settlement states.

Examples include:

- Processed but not settled
- Settlement missing
- Invalid payment lifecycle
- Failed payments with settlement

### Example Response

```json
{
    "items": [
        {
            "transaction_id": "...",
            "merchant_id": "...",
            "payment_status": "...",
            "settlement_status": "...",
            "reason": "Processed but not settled"
        }
    ]
}
```

---

# ❤️ Health Check

### Endpoint

```http
GET /health
```

### Example Response

```json
{
    "status": "healthy",
    "database": "connected"
}
```

---

# 🔐 Idempotency

The service guarantees idempotent event ingestion.

Duplicate requests with the same **event_id**:

- are detected automatically
- do not create duplicate records
- do not corrupt transaction state
- preserve data consistency

This is implemented using a unique event identifier and duplicate event validation before processing.

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

# 💾 Database Design

The database is normalized into three core entities.

| Table | Purpose |
|--------|----------|
| merchants | Merchant information |
| transactions | Current transaction state |
| payment_events | Immutable event history |

This avoids duplicated merchant data while preserving a complete audit trail for every transaction.

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

# 🤝 Trade-offs

To keep the implementation focused on the assignment requirements, the following features were intentionally excluded.

| Feature | Reason |
|----------|--------|
| Authentication | Outside assignment scope |
| Authorization | Outside assignment scope |
| Background workers | REST processing is sufficient |
| Message queues | Added complexity without requirement |
| Distributed caching | Dataset size does not justify caching |
| Rate limiting | Not requested |
| Multi-region deployment | Outside scope |

These would be natural additions in a production-scale system.

---

# 📸 Screenshots

> Replace these placeholders before submission.

| Screenshot | File |
|------------|------|
| Swagger Documentation | docs/images/swagger.png |
| Transactions API | docs/images/transactions.png |
| Transaction Details | docs/images/transaction-details.png |
| Reconciliation Summary | docs/images/reconciliation-summary.png |
| Discrepancies API | docs/images/discrepancies.png |
| Docker Containers | docs/images/docker.png |
| Render Deployment | docs/images/render.png |
| Automated Tests | docs/images/tests.png |

---

# 🎥 Demo

A walkthrough demonstrating:

- Project overview
- Local setup
- Docker deployment
- Live Render deployment
- Event ingestion
- Transaction APIs
- Reconciliation APIs
- Health endpoint
- Test execution

📹 **Demo Video**

> `<ADD_LOOM_OR_YOUTUBE_LINK>`

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