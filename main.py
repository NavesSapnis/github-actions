from aiogram import Bot, Dispatcher
from confing import BOT_TOKEN
from aiogram.types import Message



bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


@dp.message()
async def start(message: Message):
    await message.answer("hello")
