from Database import sqlite_db
from aioadverts import get_news
from sender import AdKrisha
import asyncio, aiohttp, bs4
from create_bot import bot


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