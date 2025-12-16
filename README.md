# 🧠 ToDo – Clean Architecture Reference Project

Purpose: This repository is created as a code review & learning reference to understand how Clean Architecture and Clean Code principles can be applied in a real-world backend project using Python + FastAPI.

The goal is not feature richness, but clarity of architecture, boundaries, and responsibilities.

## 🎯 Why this repository exists

Many projects mention Clean Architecture, but the implementation details are often unclear or mixed with framework logic.

This repository is designed to:

📖 Serve as a reviewable codebase for Clean Architecture

🧩 Show clear separation of concerns

🔄 Demonstrate dependency inversion in practice

🧪 Make the core business logic framework-agnostic and testable

👀 Be suitable for code review, mentoring, and interviews

## 🧱 Architectural Style

This project follows Clean Architecture (Robert C. Martin) principles:


<p align="center">
  <img src="CleanArchitecture.jpg" alt="Alternative Text for Accessibility" width="500" style="display: block; margin: 0 auto;">
</p>

### Key rules

- Domain has no dependency on any external layer

- Application depends only on Domain abstractions

- Infrastructure implements interfaces defined in Domain

- Presentation orchestrates use cases but contains no business logic

- Dependencies always point inward.

##  📂 Project Structure
```
project/
│
├── domain/
│   ├── entities/
│   │   ├── users.py
│   │   ├── tasks.py
│   │   └── passwords.py
│   │   └── __init__.py

│   │
│   ├── services/
│   │   ├── password_hasher.py
│   │   ├── normalizers.py 
│   │   └── __init__.py
│   │
│   ├── interfaces/
│   │   ├── user_repository.py   
│   │   ├── task_repository.py
│   │   ├── jwt_provider.py
│   │   └── __init__.py
│   │
│   └── __init__.py
│
├── application/
│   ├── use_cases/
│   │   ├── create_user_usecase.py
│   │   ├── update_user_usecase.py
│   │   ├── retrieve_user_usecase.py
│   │   ├── create_task_usecase.py
│   │   ├── update_task_usecase.py
│   │   ├── retrieve_task_usecase.py
│   │   ├── delete_task_usecase.py
│   │   └── __init__.py
│   │
│   ├── dtos/
│   │   ├── user_dto.py
│   │   ├── task_dto.py
│   │   └── __init__.py
│   │
│   └── __init__.py
│
├── infrastructure/
│   ├── db/
│   │   ├── postgres/
│   │   │   ├── connection.py
│   │   │   ├── user_repository_postgres.py
│   │   │   ├── task_repository_postgres.py
│   │   │   └── migrations/
│   │   │       ├── 001_init.sql
│   │   │       └── ...
│   │   ├── alembic/
│   │   │   ├── env.py
│   │   │   ├── alembic.ini
│   │   │   ├── script.py.mako
│   │   │   └── versions//
│   │   │       ├── 001_init.sql
│   │   │       └── ...
│   │   ├── auth/
│   │   │   ├── __init__.py
│   │   │   ├── password_hasher_passlib.py
│   │   │   ├──
│   │   │   
│   │   │
│   │   └── sqlalchemy_engine.py
│   │   └── __init__.py
│   │  
│   │
│   ├── 
│   │
│   │
│   ├── config/
│   │   ├── settings.py
│   │   └── __init__.py
│   │
│   └── __init__.py
│
├── presentation/
│   ├── api/
│   │   ├── fastapi/
│   │   │   ├── main.py
│   │   │   ├── dependencies.py
│   │   │   ├── schema/
│   │   │   │   ├── task_schema.py
│   │   │   │   ├── user_schema.py
│   │   │   │   ├── auth_schema.py
│   │   │   │   └── __init__.py

│   │   │   ├── controllers/
│   │   │   │   ├── auth_controller.py
│   │   │   │   ├── task_controller.py
│   │   │   │   └── __init__.py
│   │   │   

│   │   │   └── __init__.py
│   │   │
│   │   └── __init__.py
│   
│   
│
├── tests/
│   ├── domain/
│   ├── application/
│   ├── infrastructure/
│   ├── interfaces/
│   └── conftest.py
│
├── docker-compose.yml  
├── Dockerfile
├── requirements.txt
├── .env
└── README.md
```




## 🧠 Layer Responsibilities
### 1️⃣ Domain Layer (Core)

#### What lives here:

- Entities (User, Task, Password)

- Domain services (e.g. password rules, normalization)

- Interfaces (Repository, JWT provider, Password hasher)

#### What is NOT allowed:

- FastAPI

- SQLAlchemy

- Passlib / JWT libraries

- Environment variables

This layer represents pure business logic.

### 2️⃣ Application Layer (Use Cases)

#### What lives here:

- Use cases like CreateUser, UpdateTask, RetrieveUser

- DTOs for controlled data flow

#### Responsibilities:

- Orchestrate domain logic

- Enforce application-specific rules

- Communicate through interfaces, not implementations

- One use case = one business action.

#### 3️⃣ Infrastructure Layer (Details)

#### What lives here:

- Database connection (PostgreSQL, SQLAlchemy)

- Repository implementations

- Password hashing (Passlib)

- JWT implementation

- Alembic migrations

#### Key idea:

Infrastructure depends on Domain — never the other way around.

### 4️⃣ Presentation Layer (FastAPI)

#### What lives here:

- Controllers (HTTP endpoints)

- Request/response schemas

- Dependency injection

#### Responsibilities:

- Translate HTTP → Use Case input

- Return Use Case output → HTTP response

- No business logic here.

## 🧪 Testing Strategy

Tests follow the same architectural boundaries:
```bash
tests/
├── domain/ # Pure unit tests
├── application/ # Use case tests (mocked interfaces)
├── infrastructure/# Integration tests
└── presentation/ # API-level tests
```
This allows:

- Fast unit tests

- Isolated business rule validation

- Confident refactoring

## 🐳 Running the Project
Development (Docker)
```bash 
docker-compose -f docker-compose.dev.yml up --build

```

## 🗃️ Database & Migrations (Alembic)

Create migration:

```bash
alembic -c infrastructure/db/alembic/alembic.ini revision --autogenerate -m "init tables"

```
Apply migration:

```bash
alembic -c infrastructure/db/alembic/alembic.ini upgrade head
```

## 🧩 Intended Audience

This repository is useful for:

- Backend developers learning Clean Architecture

- Developers preparing for system design / backend interviews

- Code review & mentoring sessions

- Engineers transitioning from framework-centric design to architecture-first thinking

## 🔍 How to Use This Repo

- Read layer by layer (Domain → Application → Infrastructure → Presentation)

- Review how interfaces invert dependencies

- Use it as a reference structure for your own projects

- Fork it and experiment with alternative implementations

## ✨ Final Note

- This project intentionally favors clarity over shortcuts.

- If something feels more verbose than usual — that is by design.
  
- Clean Architecture optimizes for long-term maintainability, not short-term speed.