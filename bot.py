from aiogram.utils import executor
from create_bot import dp, bot
from aiogram import types
import db


async def on_startup(_):
    print("Папа в здании ")
    db.db_start()


@dp.message_handler(commands=['start'])
async def start_window(message: types.Message):
    await bot.send_message(message.from_user.id, 'Для регистрации в сети в сообщении отправьте название вашей компании')

@dp.message_handler(lambda message: message.text.lower() != "/start")
async def add_user(message: types.Message):
    await db.user_add(message)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates = True, on_startup = on_startup)
