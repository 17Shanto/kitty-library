# Kitty Library
This is just a practice project of FastAPi. Learning core engineering and design principles

## How to start
just clone the project 😎 and
run:
```bash
#Install/check your dependencies (you already have them, but torch and torchvision are key):
pip install -r requirements.txt
#Run The Server
fastapi dev src/
```
## Api doc
```bash
http://127.0.0.1:8000/docs
```

##Example Env
```
DATABASE_URL = postgresql+asyncpg://username:password@localhost:5432/db_name
JWT_SECRET = 
JWT_ALGORITHM = HS256
ACCESS_TOKEN_EXPIRY = 3600
REDIS_HOST = localhost
REDIS_PORT = 6379
JTI_EXPIRY= 3600
```

## 🛠️ Tech Stack

### Backend & API
* **FastAPI**: A high-performance web framework for building APIs with Python, based on standard Python type hints.
* **Pydantic**: Data validation and settings management using Python type annotations.

### Database & Persistence
* **PostgreSQL**: The primary relational database for robust data storage.
* **SQLModel**: A library for interacting with SQL databases from Python code. It combines the power of **SQLAlchemy** and the simplicity of **Pydantic**.
* **SQLAlchemy**: The underlying SQL toolkit and Object Relational Mapper (ORM) used for flexible database communication.

### Caching & Event Streaming
* **Redis**: High-performance, in-memory data store used for caching and session management.
* **Apache Kafka**: A distributed event streaming platform used for building real-time data pipelines and handling asynchronous messaging.

---

### 🏗️ Architecture Overview



The following flow represents how data moves through the stack:

1.  **Request Layer**: FastAPI receives incoming requests.
2.  **Validation Layer**: Pydantic ensures data integrity before processing.
3.  **ORM Layer**: SQLModel/SQLAlchemy maps Python objects to the PostgreSQL schema.
4.  **Performance Layer**: Redis caches frequent queries to reduce latency.
5.  **Messaging Layer**: Kafka handles event-driven tasks and background processing.
