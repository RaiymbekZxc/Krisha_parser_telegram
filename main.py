
from create_bot import dp
from aiogram import executor
from Database import sqlite_db
import asyncio
from mp_of_bot import ps


async def on_startup(_):
    print("Бот начал работу!")
    sqlite_db.sql_start()
    loop = asyncio.get_event_loop()
    loop.create_task(ps())


from Handlers import commands, filter_register
commands.register_handlers_commands(dp)
filter_register.register_handlers_filters(dp)


executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
