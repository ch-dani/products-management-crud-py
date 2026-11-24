# 🛍️ Product Management API (FastAPI Template)

A clean, modular, and extensible **REST API template for Product Management**, built with **Python 3**, **FastAPI**, **SQLAlchemy 2.0**, and **PostgreSQL**.

Designed as a modern starter boilerplate following professional architectural patterns: clean separation of concerns, data validation with Pydantic v2, standardized response wrappers, and database migrations with Alembic.

---

## 📋 Table of Contents

- [Overview](#-overview)
- [Tech Stack](#-tech-stack)
- [Project Architecture](#-project-architecture)
- [Database Schema](#-database-schema)
- [Getting Started](#-getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation & Setup](#installation--setup)
  - [Database Migrations](#database-migrations)
  - [Running the Application](#running-the-application)
- [API Documentation & Endpoints](#-api-documentation--endpoints)
  - [Products](#products)
  - [Product Categories](#product-categories)
  - [Response Envelope Format](#response-envelope-format)
- [Database Migrations with Alembic](#-database-migrations-with-alembic)
- [Roadmap & Next Steps](#-roadmap--next-steps)
- [License](#-license)

---

## 🌟 Overview

This project serves as a foundational boilerplate for e-commerce or inventory backends. Key highlights include:

- **Layered Architecture**: Clear isolation between HTTP routing, controllers, business services, and database persistence.
- **Modern ORM (SQLAlchemy 2.0)**: Uses type-safe `Mapped` and `mapped_column` definitions.
- **Pydantic v2 Validation**: Request data validation, automated schema enforcement, and camelCase serialization.
- **Unified API Response Envelope**: Consistent JSON response format (`APIResponse[T]`) across endpoints.
- **Interactive API Documentation**: Auto-generated Swagger UI (`/docs`) and ReDoc (`/redoc`).
- **Database Migrations**: Version-controlled database schema using Alembic.

---

## 🛠️ Tech Stack

| Technology | Purpose |
| :--- | :--- |
| **[Python 3.10+](https://www.python.org/)** | Core programming language |
| **[FastAPI](https://fastapi.tiangolo.com/)** | High-performance asynchronous web framework |
| **[SQLAlchemy 2.0](https://www.sqlalchemy.org/)** | Modern Object-Relational Mapping (ORM) |
| **[Alembic](https://alembic.sqlalchemy.org/)** | Database migrations tool |
| **[PostgreSQL](https://www.postgresql.org/)** | Relational database |
| **[Psycopg 3](https://www.psycopg.org/psycopg3/)** | Modern PostgreSQL database adapter for Python |
| **[Pydantic v2](https://docs.pydantic.dev/)** | Data validation and settings management |
| **[Uvicorn](https://www.uvicorn.org/)** | Lightning-fast ASGI web server |
| **[python-dotenv](https://github.com/theskumar/python-dotenv)** | Environment variable loading from `.env` |

---

## 🏗️ Project Architecture

The project is structured following the **Layered (N-Tier) Architecture** pattern:

```text
product-mg-py/
├── alembic/                      # Alembic migration environment and scripts
│   ├── versions/                 # Version migration files (DDL history)
│   └── env.py                    # Alembic runtime configuration
├── app/
│   ├── controllers/              # Controller layer (handles input & invokes services)
│   │   └── admin_controllers/    # Admin-specific controllers
│   │       ├── product_controller.py
│   │       ├── product_category_controller.py
│   │       └── product_specs_controller.py
│   ├── db/                       # Database engine & session management
│   │   ├── base.py               # DeclarativeBase class
│   │   └── database.py           # Engine, SessionLocal, get_db dependency
│   ├── models/                   # SQLAlchemy ORM database models
│   │   ├── Product.py            # Products table model
│   │   ├── ProductCategory.py    # Categories table model
│   │   └── ProductSpecs.py       # Product specifications table model
│   ├── schemas/                  # Pydantic validation & response schemas
│   │   ├── product_schema.py     # Request/response DTOs for products
│   │   └── response_wrapper.py   # Generic APIResponse[T] wrapper
│   └── services/                 # Business logic and database operations
│       └── product_service.py    # Service methods for products
├── routers/                      # FastAPI endpoint definitions & route grouping
│   ├── product_router.py         # Routes under /products
│   └── product_category_router.py# Routes under /product_categories
├── .env                          # Local environment variables (do not commit!)
├── .env.example                  # Template for environment variables
├── alembic.ini                   # Alembic configuration file
├── main.py                       # Application entry point & router mounting
└── requirements.txt              # Project dependencies
```

### Request Flow

```
[ Client Request ]
       │
       ▼
 [ FastAPI Router ]        (e.g., routers/product_router.py)
       │
       ▼
  [ Controller ]           (e.g., app/controllers/admin_controllers/product_controller.py)
       │
       ▼
    [ Service ]            (e.g., app/services/product_service.py - business logic)
       │
       ▼
 [ Database / Model ]      (e.g., app/models/Product.py via SQLAlchemy Session)
       │
       ▼
[ Response Envelope ]      (app/schemas/response_wrapper.py -> JSON output)
```

---

## 🗄️ Database Schema

The database currently includes three core entities:

1. **`products`**
   - `id` (Integer, Primary Key)
   - `category_id` (Integer, Optional)
   - `title` (String(100), Required)
   - `created_at` (DateTime, Server Default `now()`)
   - `updated_at` (DateTime, Optional, Auto-updated on modification)

2. **`product_categories`**
   - `id` (Integer, Primary Key)
   - `category_id` (Integer, Optional, for nested/parent categories)
   - `title` (String(500), Required)
   - `created_at` (DateTime, Server Default `now()`)
   - `updated_at` (DateTime, Optional)

3. **`product_specs`**
   - `id` (Integer, Primary Key)
   - `ps_key` (String(100), Required - e.g., "Color", "RAM", "Weight")
   - `ps_value` (String(100), Required - e.g., "Midnight Blue", "16GB")
   - `created_at` (DateTime, Server Default `now()`)

---

## 🚀 Getting Started

### Prerequisites

- **Python**: Version 3.10 or higher
- **PostgreSQL**: Installed and running locally or via Docker / cloud instance

### Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd product-mg-py
   ```

2. **Create and activate a virtual environment:**
   ```bash
   # On macOS/Linux:
   python3 -m venv venv
   source venv/bin/activate

   # On Windows (Command Prompt):
   venv\Scripts\activate.bat

   # On Windows (PowerShell):
   venv\Scripts\Activate.ps1
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables:**
   Copy `.env.example` to create your `.env` file:
   ```bash
   cp .env.example .env
   ```
   Open `.env` and configure your PostgreSQL database connection string:
   ```env
   DATABASE_URL=postgresql+psycopg://<username>:<password>@localhost:5432/<database_name>
   ```

### Database Migrations

Apply the database schema to your PostgreSQL database using Alembic:

```bash
alembic upgrade head
```

### Running the Application

Start the local development server with live reload:

```bash
uvicorn main:app --reload
```

The server will be available at: **`http://127.0.0.1:8000`**

---

## 📖 API Documentation & Endpoints

Once the application is running, explore the interactive documentation:

- **Swagger UI**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **ReDoc**: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

### Summary of Endpoints

#### Products (`/products`)

| Method | Endpoint | Description | Request Body |
| :--- | :--- | :--- | :--- |
| `GET` | `/products/` | List all products | None |
| `POST` | `/products/` | Create a new product | `ProductCreate` JSON |
| `POST` | `/products/{id}/update` | Update an existing product | Product fields |
| `DELETE` | `/products/{id}` | Delete a product | None |

#### Product Categories (`/product_categories`)

| Method | Endpoint | Description | Request Body |
| :--- | :--- | :--- | :--- |
| `GET` | `/product_categories/` | List all product categories | None |
| `POST` | `/product_categories/` | Create a new product category | Category JSON |
| `POST` | `/product_categories/{id}/update` | Update a category | Category fields |
| `DELETE` | `/product_categories/{id}` | Delete a category | None |

### Response Envelope Format

All standard responses are wrapped in a unified structure:

```json
{
  "success": true,
  "message": "Product created successfully",
  "data": {
    "id": 1,
    "categoryId": 2,
    "title": "Wireless Mechanical Keyboard",
    "createdAt": "2026-11-24T10:00:00Z"
  }
}
```

> **Note**: Field names in the `data` payload automatically serialize to `camelCase` for clean consumption by frontend applications (e.g., React, Vue, Angular).

---

## 🔄 Database Migrations with Alembic

When you modify SQLAlchemy models in `app/models/`, use Alembic to generate and apply migrations:

```bash
# 1. Generate a new migration script automatically
alembic revision --autogenerate -m "describe your changes"

# 2. Review the generated file inside alembic/versions/

# 3. Apply the migration to the database
alembic upgrade head

# 4. Roll back the last migration (if needed)
alembic downgrade -1
```

---

## 🗺️ Roadmap & Next Steps

Recommended enhancements for extending this template:

- [ ] Complete full CRUD service implementation for categories and product specs.
- [ ] Add explicit SQLAlchemy `ForeignKey` relationships between `Product`, `ProductCategory`, and `ProductSpecs`.
- [ ] Add pagination (`page`, `page_size`), sorting, and search filtering.
- [ ] Implement global exception handlers (e.g., for `404 Not Found` and database errors).
- [ ] Add user authentication & authorization (JWT / OAuth2).
- [ ] Add Dockerfile & `docker-compose.yml` for containerized development.
- [ ] Add automated tests using `pytest` and `httpx`.

---

## 📄 License

This project is licensed under the [MIT License](LICENSE) (or your preferred license).
