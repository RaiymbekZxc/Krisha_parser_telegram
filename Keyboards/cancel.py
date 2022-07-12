from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

b = KeyboardButton('Отмена')
cancel_only = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

cancel_only.add(b)