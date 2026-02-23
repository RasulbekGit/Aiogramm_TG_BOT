import asyncio

from aiogram import Bot, Dispatcher

from config import config
from routers import router as main_router


async def main():
    bot = Bot(token=config.bot_token.get_secret_value())
    dp = Dispatcher()
    dp.include_router(main_router)

    print("Bot is running...")
    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Bot stopped")
