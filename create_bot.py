
from aiogram import Dispatcher, Bot
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage()

token = '5218637762:AAHLCFsfSICJfWQoepS4ixwkCuLMpvjKJVY'
bot = Bot(token='5218637762:AAHLCFsfSICJfWQoepS4ixwkCuLMpvjKJVY')
dp = Dispatcher(bot, storage=storage)
