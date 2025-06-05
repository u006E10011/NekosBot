import asyncio
import os
from aiogram import Bot, Dispatcher, F
from app.handler import router
from dotenv import load_dotenv


async def main():
    print("Enable Bot")
    load_dotenv()
    bot = Bot(os.getenv("TOKEN"))
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Disable Bot")
