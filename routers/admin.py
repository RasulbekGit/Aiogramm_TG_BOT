from aiogram import F, Router, types

from config import config

router = Router()


@router.message(F.from_user.id == config.admin_id, F.text == "me")
async def send_message_for_user_id(message: types.Message):
    await message.answer("Salem sen Rasulsan")
