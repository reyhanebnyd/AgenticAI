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

### 1. Go to Messages directory
```bash
cd Messages
```
### 2. Create .env file
Create a .env file in the (Messages/) and add:
```bash
SECRET_KEY=your_django_secret_key_here
```

### 3 .Apply migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 4. Run the Server
```bash
python manage.py runserver
```



