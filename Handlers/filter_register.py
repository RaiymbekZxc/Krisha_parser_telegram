
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from create_bot import bot
from aiogram import Dispatcher, types
from Keyboards import district, room_kb, on_start, cancel_only, kb_client
from Database import sqlite_db


class FSMFilter(StatesGroup):
    filter = State()
    square_info = State()
    price_info = State()
    district = State()
    rooms = State()


def intcheck(num):
    try:
        int(num)
        return True
    except:        
        return False


async def cm_start(message: types.Message):
    await FSMFilter.filter.set()
    await bot.send_message(message.from_user.id, 'Фильтр под каким номером вы хотите ввести?', reply_markup=kb_client)


async def load_filter_num(message: types.Message, state: FSMContext):
    if str(message.text).lower() == 'отмена':
        await state.finish()
    else:
        if intcheck(message.text):
            if 0 < int(message.text) < 4:
                async with state.proxy() as data:
                    data['sender_id_filter'] = str(message.from_user.id) + str(message.text)
                await FSMFilter.next()
                await bot.send_message(message.from_user.id, 'Скольки квадратные квартиры вам интересны? Введите в формате "от до" (10 30)', reply_markup=cancel_only)
        else:
            await bot.send_message(message.from_user.id, 'Прошу вписать цирфу до 3', reply_markup=cancel_only)
 

async def load_squares(message: types.Message, state: FSMContext):
    if str(message.text).lower() == 'отмена':
        await state.finish()
    else:
        ms_info = str(message.text).split()
        if len(ms_info) == 2:
            if intcheck(ms_info[0]) and intcheck(ms_info[1]):
                if int(ms_info[0]) < int(ms_info[1]):
                    async with state.proxy() as data:
                        data['square_info'] = message.text
                    await FSMFilter.next()
                    await bot.send_message(message.from_user.id, 'В каком диапазоне цены вам нужна квартира?(Впшите в формате "10000000 20000000")', reply_markup=cancel_only)
                else:
                    await bot.send_message(message.from_user.id, 'Верхняя планка должна быть больше чем нижняя!', reply_markup=cancel_only)
            else: 
                await bot.send_message(message.from_user.id, 'Нужно чтобы и то и другое было цифрами!', reply_markup=cancel_only)
        else:
            await bot.send_message(message.from_user.id, 'Нужно вводить 2 цирфы через пробел!', reply_markup=cancel_only)
    

async def load_price(message: types.Message, state: FSMContext):
    pr_info = str(message.text).split()
    if str(message.text).lower() == 'отмена':
        await state.finish()
    else:
        if len(pr_info) == 2:
            if intcheck(pr_info[0]) and intcheck(pr_info[1]):
                if int(pr_info[0]) < int(pr_info[1]):
                    async with state.proxy() as data:
                        data['price_info'] = message.text
                    await FSMFilter.next()
                    await bot.send_message(message.from_user.id, 'В каком районе вам нужно искать?', reply_markup=district)
                else:
                    await bot.send_message(message.from_user.id, 'Верхняя планка цены должна быть больше нижней!', reply_markup=district)
            else:
                await bot.send_message(message.from_user.id, 'Нужно чтобы и то и другое было цифрами!', reply_markup=district)
        else:
            await bot.send_message(message.from_user.id, 'Нужно вводить 2 цирфы через пробел, вам придется вводить фильтр заново!', reply_markup=district)


async def load_district(message : types.Message, state: FSMContext):
    if str(message.text).lower() == 'отмена':
        await state.finish()
    else:
        districts = ('ауэзовский', 'алатауский', 'турксибский', 'жетысуйский', 'медеуский', 'наурызбайский', 'бостандыкский', 'алмалинский')
        if str(message.text).lower().strip() in districts:
            async with state.proxy() as data:
                data['district'] = message.text
            await FSMFilter.next()
            await bot.send_message(message.from_user.id, 'Сколько комнтаные квартиры вас интересуют?', reply_markup=room_kb)
        else:
            await bot.send_message(message.from_user.id, 'Данного района нет в списке доступных', reply_markup=room_kb)


async def load_rooms(message: types.Message, state: FSMContext):
    if str(message.text).lower() == 'отмена':
        await state.finish()
    else:
        if intcheck(message.text):
            async with state.proxy() as data:
                data['rooms'] = message.text
                data['active'] = 1
        await FSMFilter.next()
        await sqlite_db.sql_add_command(state)
        await bot.send_message(message.from_user.id, "Вы успешно ввели фильтр(если внизу не появилось сообщение об ошибке)", reply_markup=on_start)
        await state.finish()


def register_handlers_filters(dp: Dispatcher):
    dp.register_message_handler(cm_start, lambda message: 'поставить фильтр' == str(message.text).strip().lower(), state=None)
    dp.register_message_handler(load_filter_num, state=FSMFilter.filter)
    dp.register_message_handler(load_squares, state=FSMFilter.square_info)
    dp.register_message_handler(load_price, state=FSMFilter.price_info)
    dp.register_message_handler(load_district, state=FSMFilter.district)
    dp.register_message_handler(load_rooms, state=FSMFilter.rooms)
    