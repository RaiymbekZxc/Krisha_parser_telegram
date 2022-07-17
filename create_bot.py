
from aiogram import Dispatcher, Bot
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage()

token = '5218637762:AAHLCFsfSICJfWQoepS4ixwkCuLMpvjKJVY'
bot = Bot(token=token)
dp = Dispatcher(bot, storage=storage)
