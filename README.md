🎬 Movie Watchlist Tracker API

A production-ready Movie Watchlist REST API built with FastAPI, Async SQLAlchemy 2.0, PostgreSQL, and Dependency Injection.

Designed using a clean layered architecture (Controller → Logic → Repository) and fully containerized with Docker.

**********************************************************************************************************
🚀 Features

Create, update, delete movies

Filter movies by status, genre, and rating

Movie statistics endpoint (total, watched, average rating)

Async SQLAlchemy 2.0 support

PostgreSQL database

Dependency Injection (using dependency-injector)

Docker & Docker Compose ready

Poetry-based dependency management

Clean architecture principles

**************************************************************************************************************
🏗 Architecture

The project follows a layered architecture pattern:

src/
 ├── controllers/        # FastAPI routers (HTTP layer)
 ├── logics/             # Business logic layer
 ├── repositories/       # Database access layer
 ├── models/             # SQLAlchemy models
 ├── schemas/            # Pydantic schemas
 ├── configs/            # Configuration & DI container

Layer Responsibilities
Layer	Responsibility
Controller	Handles HTTP requests and responses
Logic	Business rules & validations
Repository	Database interaction
Model	SQLAlchemy entities
Schema	Request/Response validation (Pydantic)

**************************************************************************************************************
🧰 Tech Stack

Python 3.13

FastAPI

SQLAlchemy 2.0 (Async)

PostgreSQL 15

asyncpg

Pydantic v2

Dependency Injector

Archipy

Poetry

Docker

**************************************************************************************************************
⚙️ Environment Variables

Create a .env file in the root directory:

DATABASE_URL=postgresql+asyncpg://project_user:StrongProjectPassword123@localhost/project_db
ECHO=False
🐳 Running with Docker (Recommended)
1️⃣ Build & Start
docker compose up --build
2️⃣ Access the API

API Base URL:

http://localhost:8000

Swagger Documentation:

http://localhost:8000/docs
💻 Running Locally (Without Docker)
1️⃣ Install dependencies
poetry install

2️⃣ Activate environment
eval $(poetry env activate)

3️⃣ Run the application
uvicorn main:app --reload

**************************************************************************************************************
📡 API Endpoints

Base URL:

/api/v1/movies

**************************************************************************************************************
🎬 Create Movie

POST /

{
  "title": "Inception",
  "genre": "Sci-Fi",
  "release_year": 2010,
  "status": "want_to_watch"
}
📃 List Movies

GET /

Query Parameters
Parameter	Type	Description
status	string	watched or want_to_watch
genre	string	Filter by genre
rating	integer (1-5)	Filter by rating

Example:

GET /api/v1/movies?status=watched

**************************************************************************************************************
🔎 Get Movie By ID
GET /api/v1/movies/{movie_uuid}

**************************************************************************************************************
✏️ Update Movie
PUT /api/v1/movies/{movie_uuid}

Example body:

{
  "rating": 5,
  "status": "watched",
  "notes": "Amazing movie!"
}

**************************************************************************************************************
❌ Delete Movie
DELETE /api/v1/movies/{movie_uuid}

**************************************************************************************************************
📊 Get Statistics
GET /api/v1/movies/stats

Response:

{
  "total_movies": 10,
  "watched_movies": 6,
  "average_rating": 4.2
}

**************************************************************************************************************
🗄 Database Design
Movie Entity Fields

movie_uuid (UUID, Primary Key)

title (String, required)

genre (String, optional)

release_year (Integer, optional)

status (Enum: watched | want_to_watch)

rating (Integer 1–5, optional)

notes (String, optional)

created_at (Datetime)

Tables are automatically created on application startup.

**************************************************************************************************************

🧩 Dependency Injection

The project uses dependency-injector for clean service wiring:

class ServiceContainer(containers.DeclarativeContainer):
    session = providers.Factory(AsyncSessionFactory)
    movie_repository = providers.Factory(MovieRepository, session=session)
    movie_logic = providers.Factory(MovieLogic, movie_repository=movie_repository)
Benefits

Loose coupling

Easy unit testing

Clear separation of concerns

Scalable architecture

🛠 Docker Services
Service	Description	Port
api	FastAPI application	8000
db	PostgreSQL 15	5432

**************************************************************************************************************
🔮 Future Improvements

Pagination support

Sorting support

Authentication & Authorization

Unit & integration tests

Alembic database migrations

CI/CD pipeline


**************************************************************************************************************
📄 License

This project is open-source and available under the MIT License.

