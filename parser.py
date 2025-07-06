import os 

from telethon import TelegramClient
from telethon.sessions import StringSession
from dotenv import load_dotenv

from config import KEYWORDS, CHANNELS

load_dotenv()

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
SESSION = os.getenv("TELETHON_SESSION")

chanels = CHANNELS

client = TelegramClient(StringSession(SESSION), API_ID, API_HASH)


async def get_air_warning_message(channels):
    message = []
    async for chanel in client.iter_messages(channels, limit= 2):
        text = chanel.text or ""
        if any(kw.lower() in text.lower() for kw in KEYWORDS):
            message.append(chanel.text)
    return message

