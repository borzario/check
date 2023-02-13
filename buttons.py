from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


b_userID = KeyboardButton("Узнать свой айди")
b_putID = KeyboardButton("Добавить свой айди в базу")
kb_main = ReplyKeyboardMarkup(resize_keyboard=True)
kb_main.row(b_userID).row(b_putID)