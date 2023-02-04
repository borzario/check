from aiogram import Bot
from aiogram.dispatcher import Dispatcher
import os
from aiogram.contrib.fsm_storage.memory import MemoryStorage

#import token
import autofication

storage = MemoryStorage()
bot = Bot(token = autofication.TOKEN)
dp = Dispatcher(bot, storage=storage)