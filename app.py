import asyncio

from aiogram import Bot, Dispatcher, executor
from config import *

loop = asyncio.new_event_loop()
bot = Bot(TOKEN, parse_mode="HTML")
dp=Dispatcher(bot, loop=loop)

if __name__=="__main__":
    from handlers import *
    executor.start_polling(dp, skip_updates=True)
