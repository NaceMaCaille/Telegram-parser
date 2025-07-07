import os
import asyncio

from aiogram import Bot, Dispatcher
from dotenv import load_dotenv

from handlers import periodic_air_check
from parser import client

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")

chat = '@chernihiv_air_warning'

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


async def main():
    await client.connect()
    
    asyncio.create_task(periodic_air_check(bot, chat))
    
    await dp.start_polling(bot)
    
    
if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt as e:
        print("Вихід з програми")
    