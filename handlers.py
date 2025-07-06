import asyncio
import os

from aiogram import Bot
from dotenv import load_dotenv

from config import CHANNELS
from parser import get_air_warning_message

load_dotenv()

CHAT_ID = int(os.getenv('CHAT_ID'))


async def check_and_send_air_warning(bot: Bot):
    res = []
    for channel in CHANNELS:
        texts = await get_air_warning_message(channel)
        for text in texts:
            res.append(f'Канал {channel} повідомляє:\n{text}')
    if res:
        await bot.send_message(chat_id=CHAT_ID, text="\n\n".join(res))
    else:
        await bot.send_message(chat_id=CHAT_ID, text="Зараз тихо")
    
    
async def periodic_air_check(bot: Bot, chat_id: int):
    while True:
        await check_and_send_air_warning(bot, chat_id)
        await asyncio.sleep(150)

