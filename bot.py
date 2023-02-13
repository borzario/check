from aiogram.utils import executor
from create_bot import dp, bot
from aiogram import types
import db
import buttons

async def on_startup(_):
    print("Папа в здании ")
    db.db_start()


@dp.message_handler(commands=['start'])
async def start_window(message: types.Message):
    await bot.send_message(message.from_user.id, 'Выберите интересующую вас функцию', reply_markup=buttons.kb_main)

@dp.message_handler(lambda message: "Узнать свой айди" in message.text)
async def add_user(message: types.Message):
    await bot.send_message(message.from_user.id, f'Ваш ID - {message.from_user.id}')

@dp.message_handler(lambda message: "Добавить свой айди в базу" in message.text)
async def add_user(message: types.Message):
    await bot.send_message(message.from_user.id, "Отправьте боту название вашей компании (при его остуствии "
                                                 "любое сообщение")

@dp.message_handler(lambda message: message.text.lower() not in ["/start", "Узнать свой айди", "Добавить свой айди в базу"])
async def add_user(message: types.Message):
    await db.user_add(message)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates = True, on_startup = on_startup)
