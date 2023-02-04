import sqlite3 as sq
import create_bot

def db_start():
    global base, cur
    base = sq.connect("users.db")
    cur = base.cursor()
    if base:
        print("Connected to bd is OK!")
    base.execute('CREATE TABLE IF NOT EXISTS users(user_id TEXT PRIMARY KEY, user_name TEXT, user_company TEXT)')
    base.commit()

async def user_add(message):
    try:
        await cur.execute("INSERT INTO users VALUES (?, ?, ?)", (message.from_user.id,  message.from_user.username, message.text))
        await create_bot.bot.send_message(5097527515,
                               f"Новый пользователь {message.from_user.username} {message.from_user.id} {message.text}")
        await create_bot.bot.send_message(message.from_user.id, "Ваш айди добавлен в базу данных")
        print("Пользователь добавлен")
    except:
        print("Повторное обращение")
        await create_bot.bot.send_message(message.from_user.id, "Ваш айди был добавлен в базу данных ранее")
    base.commit()