from aiogram import F, Router, types
from aiogram.enums.chat_action import ChatAction
from aiogram.filters import Command
from aiogram.types import FSInputFile

router = Router()


@router.message(F.photo)
async def photo_handler(message: types.Message):
    await message.answer("I cant view photo!")


@router.message(Command("image"))
async def image_cmd(message: types.Message):
    # img_url = (
    #     "https://cs14.pikabu.ru/post_img/2023/10/10/6/og_og_1696928113214795976.jpg"
    # )
    cat_image_path = "C:\\Users\\Asus\\Pictures\\photo_2025-06-03_17-08-19.jpg"
    image = FSInputFile(cat_image_path)
    await message.bot.send_chat_action(
        chat_id=message.chat.id,
        action=ChatAction.UPLOAD_PHOTO,
    )
    await message.answer_photo(
        photo=image,
        caption="my photo",
    )


@router.message(Command("doc"))
async def document_cmd(message: types.Message):
    doc = FSInputFile("C:\\Users\\Asus\\Documents\\hello.txt")
    await message.bot.send_chat_action(
        chat_id=message.chat.id,
        action=ChatAction.UPLOAD_DOCUMENT,
    )
    await message.answer_document(
        document=doc,
        caption="my document",
    )
