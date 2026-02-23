from aiogram import F, Router, types
from aiogram.filters import Command, CommandStart

router = Router()


@router.message(CommandStart())
async def cmd_start(message: types.Message):
    await message.answer(
        f"Salem, {message.from_user.full_name}!, {message.from_user.id} Bot start aldi."
    )


@router.message(Command("info"))
async def send_info(message: types.Message):
    await message.answer(f"Aiogram bot {message.web_app_data}")


@router.message(F.text == "hello")
async def send_message_hi(message: types.Message):
    await message.answer("Hi")
