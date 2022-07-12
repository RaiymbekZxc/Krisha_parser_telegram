
from aiogram import Dispatcher, types
from create_bot import bot
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from Keyboards import on_start, kb_client
from Database import sqlite_db


class FSMFilt(StatesGroup):
    filter = State()


async def command_start(message: types.Message):
    await bot.send_message(message.from_user.id, 'Вас приветствует бот для получения молниеностных объявлений с krisha.kz!', reply_markup=on_start)


async def command_help(message: types.Message):
    with open('help.txt', 'r') as help:
        await bot.send_message(message.from_user.id, help.read(), reply_markup=on_start)
    await sqlite_db.get_users_filters(message.from_user.id)


async def command_deactivate_filters(message: types.Message):
    await FSMFilt.filter.set()
    await bot.send_message(message.from_user.id, 'Какой фильтр вы хотите удалить?', reply_markup=kb_client)


async def deactivate(message: types.Message, state: FSMContext):
    filter_num = int(str(message.text()).strip())
    sender_id_filter = str(message.from_user.id) + str(filter_num)
    print(sender_id_filter)
    sqlite_db.deactivate_filter(sender_id_filter)
    await state.finish()


def register_handlers_commands(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=['start'])
    dp.register_message_handler(command_help, commands=['help'])
    dp.register_message_handler(command_deactivate_filters, commands=['deactivate'], state=None)
    dp.register_message_handler(deactivate, state=FSMContext)
