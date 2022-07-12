
import sqlite3 as sq
import asyncio

def sql_start():
    global cur, base
    base = sq.connect('fll.db')
    cur = base.cursor()
    if base:
        print("Database connection is OK!")
    else:
        print("Something went wrong")

    base.execute("CREATE TABLE IF NOT EXISTS felt(sender_id_filter TEXT PRIMARY KEY, square TEXT, price TEXT, district TEXT, rooms TEXT, active TEXT)")
    base.commit()



async def sql_add_command(state):
    async with state.proxy() as data:
        try:
            cur.execute('INSERT INTO felt VALUES(?, ?, ?, ?, ?, ?)', tuple(data.values()))
            base.commit()
        except:
            val = tuple(data.values())
            vali = []
            vali.append(val[1])
            vali.append(val[2])
            vali.append(val[3])
            vali.append(val[4])
            vali.append("1")
            vali.append(val[0])
            vali = tuple(vali)
            cur.execute(f'UPDATE felt SET square = ? , price = ? , district = ? , rooms = ? , active = ? WHERE sender_id_filter = ?', vali)
            base.commit()


async def get_active_filters():
    return cur.execute('SELECT * FROM felt WHERE active = 1')


async def deactivate_filter(sender_id_filter):    
    print(sender_id_filter)
    cur.execute('UPDATE felt SET active = 0 WHERE sender_id_filter = ?', (sender_id_filter, ))


async def get_users_filters(id):
    for i in range(1, 4):
        print((cur.execute('SELECT * FROM felt WHERE sender_id_filter = ?', (str(id) + str(i), )), ))
