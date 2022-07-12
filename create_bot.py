
from aiogram import Dispatcher, Bot
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage()

bot = Bot(token='5218637762:AAHLCFsfSICJfWQoepS4ixwkCuLMpvjKJVY')
dp = Dispatcher(bot, storage=storage)
