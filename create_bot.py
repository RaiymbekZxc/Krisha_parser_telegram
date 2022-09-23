
from aiogram import Dispatcher, Bot
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage()

token = 'TOKEN'
bot = Bot(token=token)
dp = Dispatcher(bot, storage=storage)
