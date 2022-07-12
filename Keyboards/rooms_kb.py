
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

b1 = KeyboardButton('1')
b2 = KeyboardButton('2')
b3 = KeyboardButton('3')
b4 = KeyboardButton('4')
b5 = KeyboardButton('5')


room_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

room_kb.row(b1, b2, b3, b4, b5).row('Отмена')
