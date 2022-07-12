
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

b1 = KeyboardButton('Алатауский')
b2 = KeyboardButton('Алмалинский')
b3 = KeyboardButton('Ауэзовский')
b4 = KeyboardButton('Бостандыкский')
b5 = KeyboardButton('Жетысуйский')
b6 = KeyboardButton('Медеуский')
b7 = KeyboardButton('Наурызбайский')
b8 = KeyboardButton('Турксибский')



district = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

district.row(b1, b2).row(b3, b4).row(b5, b6).row(b7, b8).row('Отмена')
