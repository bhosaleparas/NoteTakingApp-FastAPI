# 📝 Note Taking API - FastAPI

A Note Taking API built with FastAPI, featuring JWT authentication, SQLite database, and complete CRUD operations for notes.

## 🚀 Features

- **🔐 Authentication**: JWT-based user authentication (signup/login)
- **📒 Notes Management**: Full CRUD operations (Create, Read, Update, Delete)
- **🔍 Search Functionality**: Search notes by title or content
- **🔒 Security**: Password hashing with argon2, secure endpoints
- **📁 Organized Structure**: Clean separation of concerns with models, schemas, and routes
- **📚 API Documentation**: Automatic OpenAPI documentation (Swagger UI & ReDoc)

## 🛠️ Technology Stack

- **FastAPI** - Modern, fast web framework for building APIs
- **SQLAlchemy** - SQL toolkit and ORM
- **SQLite** - Lightweight database (file-based)
- **JWT** - JSON Web Tokens for authentication
- **argon2** - Password hashing
- **Pydantic** - Data validation and settings management

## 📁 Project Structure

```
note_app/
├── main.py              # FastAPI application and routes
├── database.py          # Database configuration and connection
├── models.py           # SQLAlchemy models (User, Note)
├── schemas.py          # Pydantic schemas (request/response models)
├── auth.py             # Authentication and security utilities
├── crud.py             # Database CRUD operations
├── requirements.txt    # Python dependencies
└── README.md           # This file
```

## ⚙️ Installation & Setup

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### 1. Clone and Setup
```bash
git clone https://github.com/bhosaleparas/NoteTakingApp-FastAPI.git
cd NoteTakingApp

# Create and activate virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Run the Application
```bash
# Development server with auto-reload
uvicorn main:app --reload

```

### 3. Access the Application
- **API Server**: http://localhost:8000
- **Interactive API Docs (Swagger UI)**: http://localhost:8000/docs
- **Alternative API Docs (ReDoc)**: http://localhost:8000/redoc

## 📊 Database Schema

### Users Table
| Column | Type | Description |
|--------|------|-------------|
| id | Integer | Primary key |
| email | String | Unique user email |
| username | String | Unique username |
| full_name | String | User's full name |
| hashed_password | String | Hashed password |
| created_at | DateTime | Account creation timestamp |

### Notes Table
| Column | Type | Description |
|--------|------|-------------|
| id | Integer | Primary key |
| title | String | Note title |
| content | Text | Note content |
| created_at | DateTime | Note creation timestamp |
| updated_at | DateTime | Last update timestamp |
| owner_id | Integer | Foreign key to users.id |

## 🔐 Authentication Flow

1. **Sign Up**: Register new user → Returns user details
2. **Login**: Provide username/password → Returns JWT token


## 📡 API Endpoints

### Public Endpoints

| Method | Endpoint | Description | Request Body |
|--------|----------|-------------|--------------|
| POST | `/signup` | Register new user | `email`, `username`, `password`, `full_name` (optional) |
| POST | `/login` | Login and get JWT token | `username`, `password`,`email` |


### Protected Endpoints (Require JWT)

| Method | Endpoint | Description | Request Body |
|--------|----------|-------------|--------------|
| POST | `/notes/` | Create new note | `title`, `content` (optional) |
| GET | `/notes/` | Get all user's notes | - |
| GET | `/notes/{note_id}` | Get specific note | - |
| PUT | `/notes/{note_id}` | Update a note | `title` (optional), `content` (optional) |
| DELETE | `/notes/{note_id}` | Delete a note | - |
| GET | `/notes/search/{query}` | Search notes by query | - |
| GET | `/users/me` | Get current user with notes | - |



## 📝 Sample Requests/Responses

### Signup Request
```json
{
  "email": "john@example.com",
  "username": "johndoe",
  "password": "password123",
  "full_name": "John Doe"
}
```

### Signup Response
```json
{
  "id": 1,
  "email": "john@example.com",
  "username": "johndoe",
  "full_name": "John Doe",
  "created_at": "2024-01-15T10:30:00Z"
}
```

### Note Response
```json
{
  "id": 1,
  "title": "Shopping List",
  "content": "Milk, Eggs, Bread",
  "owner_id": 1,
  "created_at": "2024-01-15T10:35:00Z",
  "updated_at": "2024-01-15T11:00:00Z"
}
```

## 🔧 Configuration

### Key Settings in `auth.py`:
```python
SECRET_KEY = "your-secret-key-here"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30
```

### Database Configuration in `database.py`:
```python
SQLALCHEMY_DATABASE_URL = "sqlite:///./notes.db"
```

## 📚 Learning Resources

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [SQLAlchemy Documentation](https://docs.sqlalchemy.org/)
- [JWT.io](https://jwt.io/) - For JWT debugging
- [Postman](https://www.postman.com/) - For API testing

---

**Happy Note Taking!** 📝✨