
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

b = KeyboardButton('Поставить фильтр')
b2 = KeyboardButton('/help')


on_start = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

on_start.add(b).add(b2)
