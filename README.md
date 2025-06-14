# Django Telegram Bot Registration System

This project is a Django-based Telegram bot integration that enables users to register themselves through the `/start` command and retrieve their stored information using the `/status` command. It securely captures essential Telegram user details such as username, chat ID, and registration timestamp, and stores them in the Django database. The implementation uses asynchronous command handlers while maintaining compatibility with Django's synchronous ORM using `sync_to_async`.

Built as part of an internship assignment, the system demonstrates clean integration between Django and external APIs, secure environment management using `.env`, and modular code structure ready for deployment. The bot is fully functional, scalable, and written with professional coding standards to stand out in a competitive selection process.

---

## Features

- `/start` command to register users into the Django database  
- `/status` command to check your stored user info  
- Asynchronous Telegram handlers with Django ORM support  
- JWT-authenticated protected API endpoint with DRF  
- Public and protected API routes via DRF views  
- Secure `.env` management using `python-decouple` or `dotenv`  
- Background email task support via Celery + Redis (optional extension)

---

## Tech Stack

- **Backend**: Django 5, Django REST Framework  
- **Bot**: python-telegram-bot v20+ (async version)  
- **Database**: SQLite (easily swappable with PostgreSQL)  
- **Queue**: Redis + Celery (for background tasks)  
- **Environment**: Python 3.12, Windows 11  
- **DevOps**: `.env`, `.gitignore`, modular folder structure  

---

## ⚙Setup Instructions

### 1. Clone the repository

git clone https://github.com/your-username/django-intern-assignment.git
cd django-intern-assignment

### 2. Create and activate virtual environment

python -m venv env
env\Scripts\activate  # On Windows

### 3. Install dependencies

pip install -r requirements.txt

### 4. Add environment variables

Create a `.env` file in the root directory:

SECRET_KEY=your-django-secret-key
TELEGRAM_BOT_TOKEN=your-telegram-bot-token
DEBUG=True

### 5. Apply migrations

python manage.py makemigrations
python manage.py migrate

### 6. Run the development server

python manage.py runserver

### 7. Run the Telegram bot

python telegram_bot/run_bot.py

---

## API Endpoints

| Method | Endpoint          | Description                      | Auth Required |
| ------ | ----------------- | -------------------------------- | ------------- |
| GET    | `/api/public/`    | Public test endpoint             | No            |
| GET    | `/api/protected/` | JWT-authenticated view           | Yes           |
| POST   | `/api/token/`     | Get JWT tokens using credentials | No            |

---

## API Testing (Using cURL)

### Get JWT Token

curl -X POST http://127.0.0.1:8000/api/token/ \
  -H "Content-Type: application/json" \
  -d '{"username": "your_username", "password": "your_password"}'

### Public Endpoint

curl http://127.0.0.1:8000/api/public/

### Protected Endpoint (JWT Required)

curl http://127.0.0.1:8000/api/protected/ \
  -H "Authorization: Bearer your_access_token"

---

## Telegram Bot Commands

| Command   | Description                                     |
| --------- | ----------------------------------------------- |
| `/start`  | Registers the user in the database              |
| `/status` | Displays stored user info (chat ID, name, time) |

---

## Folder Structure (Simplified)

```
├── core/               # Django settings & app config
├── api/                # User models and API views
├── telegram_bot/       # Telegram command handlers
├── .env                # Environment variables (not committed)
├── manage.py           # Django entry point
├── requirements.txt    # Project dependencies
```

---

## Acknowledgements

Thanks to Internshala for the opportunity to build this assignment. This project showcases a complete integration between Django REST, external bots, and asynchronous task workers — with scalable code and clear structure.

---

## 📬 Contact

* ✉️ Email: [adityapujari542@gmail.com](mailto:adityapujari542@gmail.com)
* 🌐 Portfolio: [https://problemsolving.live](https://adityapujari854.github.io/My-Portfolio)
* 💼 LinkedIn: [Aditya Pujari](https://www.linkedin.com/in/adityapujari854)
