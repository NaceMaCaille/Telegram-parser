import os
import asyncio

from aiogram import Bot, Dispatcher
from dotenv import load_dotenv

from handlers import periodic_air_check
from parser import client

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


async def main():
    await client.start()
    
    asyncio.create_task(periodic_air_check(bot, chat_id='@chernihiv_air_warning'))
    
    await dp.start_polling(bot)
    
    
if __name__ == '__main__':
    asyncio.run(main())
    
    