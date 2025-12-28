# Messages API (Django REST Framework)

A simple REST API built with Django REST Framework for storing and retrieving messages.

This project is part of an internship technical task and focuses on clean structure and DRF best practices rather than complexity.

---

## Features

- Create a new message (POST)
- Retrieve a list of messages (GET)
- Retrieve a single message by ID (GET)
- Shows message status (default: "new")
- Uses SQLite (default) but can be switched to PostgreSQL

---

## Message Model

Each message contains:

- `text` — message content
- `status` — default is "new"
- `created_at` — creation timestamp (auto-generated)

---

## API Endpoints

| Method | Endpoint | Description |
|------|---------|------------|
| GET | `/messages/` | List all messages |
| POST | `/messages/` | Create a new message |
| GET | `/messages/<id>/` | Retrieve a single message |

---

## Setup Instructions

### 1. Clone the repository
```bash
git clone <repository-url>
cd django_api
```
### 2. Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate  # for Linux and Mac
venv\Scripts\activate     # Windows
```


### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Create .env file
Create a .env file in the project root (Messages/) and add:
```bash
SECRET_KEY=your_django_secret_key_here
```

### 5.Apply migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Run the Server
```bash
python manage.py runserver
```



