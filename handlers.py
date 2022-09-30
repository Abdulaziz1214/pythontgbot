from aiogram.types import Message, CallbackQuery
from keyboards import *
from app import *

@dp.message_handler(commands=["start"])
async def command_start(message: Message):
    fullname=message.from_user.full_name
    text = f"Welcome, {fullname}"
    await message.answer(text=text)