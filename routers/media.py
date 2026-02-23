from aiogram import Router, F, types

router = Router()


@router.message(F.photo)
async def send_message_photo(message: types.Message):
    await message.answer("I cant view photo")
