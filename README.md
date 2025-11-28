# MindDo
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
│   │   └── __init__.py
│   │
│   ├── interfaces/
│   │   ├── user_repository.py   # interfaces
│   │   ├── task_repository.py
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
│   │   │
│   │   └── sqlalchemy_engine.py
│   │   └── __init__.py
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
│   │   │   ├── schema/
│   │   │   │   ├── user_schema.py
│   │   │   │   ├── task_schema.py
│   │   │   │   └── __init__.py

│   │   │   ├── controllers/
│   │   │   │   ├── user_controller.py
│   │   │   │   ├── task_controller.py
│   │   │   │   └── __init__.py
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


## alembic
```bash
alembic -c infrastructure/db/alembic/alembic.ini revision --autogenerate -m "init tables"
```
```bash
alembic -c infrastructure/db/alembic/alembic.ini upgrade head

```