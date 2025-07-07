import asyncio
import os

from aiogram import Bot

from config import CHANNELS
from parser import get_air_warning_message

chat = '@chernihiv_air_warning'

async def check_and_send_air_warning(bot: Bot, chat_id):
    res = []
    for channel in CHANNELS:
        texts = await get_air_warning_message(channel)
        for text in texts:
            res.append(f'Канал {channel} повідомляє:\n{text}')
    if res:
        await bot.send_message(chat_id=chat_id, text="\n\n".join(res))
    else:
        await bot.send_message(chat_id=chat_id, text="Зараз тихо")
    
    
async def periodic_air_check(bot: Bot, chat_id):
    while True:
        await check_and_send_air_warning(bot, chat_id=chat_id)
        await asyncio.sleep(150)

