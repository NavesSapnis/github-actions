from aiogram import Bot, Dispatcher
from confing import BOT_TOKEN
from aiogram.types import Message
import asyncio



bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


@dp.message()
async def start(message: Message):
    await message.answer("hello")


async def main():
    await dp.start_polling(bot)

asyncio.run(main())
