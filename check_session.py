import os

from telethon.sync import TelegramClient
from telethon.sessions import StringSession
from dotenv import load_dotenv

load_dotenv()

api_id = int(os.getenv('API_ID'))
api_hash = os.getenv('API_HASH')

with TelegramClient(StringSession(), api_id, api_hash) as client:
    print("⚠️ Введите номер Telegram, код из Telegram и пароль (если включен)")
    print("✅ Ваша строка-сессия:\n")
    print(client.session.save())
