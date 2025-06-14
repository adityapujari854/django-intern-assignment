import os
import sys
import django
import pytz
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from asgiref.sync import sync_to_async
from django.utils.timezone import localtime

# Load environment variables from .env file
load_dotenv()

# Set up Django environment
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
django.setup()

from api.models import TelegramUser
from django.conf import settings

# Async function to create or fetch user from database
@sync_to_async
def get_or_create_user(user):
    return TelegramUser.objects.get_or_create(
        chat_id=user.id,
        defaults={
            "username": user.username,
            "first_name": user.first_name,
            "last_name": user.last_name
        }
    )

# Async function to get user status info from database
@sync_to_async
def get_user_status(chat_id):
    try:
        user = TelegramUser.objects.get(chat_id=chat_id)
        return (
            f"👤 Username: {user.username or user.first_name or 'N/A'}\n"
            f"🆔 Chat ID: {user.chat_id}\n"
            f"📅 Registered: {localtime(user.registered_at).strftime('%Y-%m-%d %I:%M %p')}"
        )
    except TelegramUser.DoesNotExist:
        return "⚠️ You are not registered in the system."

# Handler for /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    await get_or_create_user(user)
    await update.message.reply_text(
        f"Hello {user.first_name or 'there'}! You’ve been registered successfully."
    )

# Handler for /status command
async def status(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_user.id
    message = await get_user_status(chat_id)
    await update.message.reply_text(message)

# Main entry point for bot execution
if __name__ == '__main__':
    import asyncio

    # Windows-specific event loop fix
    try:
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    except Exception:
        pass

    # Build the Telegram application
    app = ApplicationBuilder()\
        .token(settings.TELEGRAM_BOT_TOKEN)\
        .build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("status", status))

    print("✅ Bot is running. Press Ctrl+C to stop.")
    app.run_polling()
