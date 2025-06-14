# Django Telegram Bot Registration System

This project is a Django-based Telegram bot integration that enables users to register themselves through the /start command and retrieve their stored information using the /status command. It securely captures essential Telegram user details such as username, chat ID, and registration timestamp, and stores them in the Django database. The implementation uses asynchronous command handlers while maintaining compatibility with Django's synchronous ORM using sync_to_async.

Built as part of an internship assignment, the system demonstrates clean integration between Django and external APIs, secure environment management using .env, and modular code structure ready for deployment. The bot is fully functional, scalable, and written with professional coding standards to stand out in a competitive selection process.

---

## Features

- `/start` command to register users into the Django database
- `/status` command to check your stored user info
- Asynchronous handlers compatible with Django’s ORM
- Secure `.env` management using `python-decouple` and `dotenv`
- Fully functional background email system using Celery + Redis (optional feature)

---

## Tech Stack

- **Backend**: Django 5, Django REST Framework
- **Bot**: python-telegram-bot v20+ (async version)
- **Database**: SQLite (can be switched to PostgreSQL)
- **Queue**: Redis + Celery (for background tasks)
- **Environment**: Python 3.12, Windows 11
- **Deployment Ready**: Modular structure, .env support, `.gitignore` and CLI commands

---

## Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/your-username/django-intern-assignment.git
cd django-intern-assignment
