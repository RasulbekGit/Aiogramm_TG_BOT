import asyncio
import os

from aiogram import Bot, Dispatcher, F, types
from aiogram.filters import CommandStart
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")

dp = Dispatcher()


@dp.message(CommandStart())
async def cmd_start(message: types.Message):
    await message.answer(
        f"Salem, {message.from_user.full_name}!, {message.from_user.id} Bot start aldi."
    )


@dp.message(F.photo)
async def send_message_photo(message: types.Message):
    await message.answer("I cant view photo")


@dp.message(F.text == "hello")
async def send_message_hi(message: types.Message):
    await message.answer("Hi")


@dp.message(F.from_user.id == 922402671 and F.text == "me")
async def send_message_for_user_id(message: types.Message):
    await message.answer("Salem sen Rasulsan")


@dp.message()
async def send_message(message: types.Message):
    await message.answer(f"{message.from_user.full_name} - {message.text}")


async def main():
    bot = Bot(token=TOKEN)
    print("Bot is running...")
    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Bot stopped")
