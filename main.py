
from create_bot import bot, dp
from aiogram import executor
from Database import sqlite_db
from aioadverts import get_news
import asyncio
from sender import AdKrisha
import bs4, aiohttp

async def ps():
    while True:
        with open('adverts.txt', 'r') as file: 
            all = file.read()
        act = await sqlite_db.get_active_filters()
        for link in await get_news():
            if link not in all:
                with open('adverts.txt', 'a') as file:
                    file.write(link + '\n')
                
                for values in act:
    
                    await asyncio.sleep(1)

                    async with aiohttp.ClientSession() as session:
                        async with session.get(link, verify_ssl = False) as response:
                            html = await response.text()
                            soup = bs4.BeautifulSoup(html, 'html.parser')
                            ad = AdKrisha(soup)

                    pr_info = str(values[2]).split()
                    sq_info = str(values[1]).split()
                    if not int(pr_info[0]) < ad.get_price() < int(pr_info[1]):
                        continue
                    if not int(sq_info[0]) < ad.get_squares() < int(sq_info[1]):
                        continue
                    if not str(values[3]).lower().strip() == ad.get_district().lower().strip():
                        continue
                    
                    
                    try:
                        await bot.send_message(values[0][:-1], link)
                    except:
                        print("User blocked us xd")
                    
        await asyncio.sleep(10)



async def on_startup(_):
    print("Бот начал работу!")
    sqlite_db.sql_start()
    loop = asyncio.get_event_loop()
    loop.create_task(ps())



from Handlers import commands, filter_register
commands.register_handlers_commands(dp)
filter_register.register_handlers_filters(dp)


executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
