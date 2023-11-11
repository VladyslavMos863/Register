import sqlite3


database = sqlite3.connect("bot.sqlite")
cursor = database.cursor()


def add_user(message):
    cursor.execute("SELECT id FROM user WHERE id=?",(message.chat.id,))
    user = cursor.fetchone()
    if not user:
        cursor.execute("INSERT INTO user VALUES(?,?,?)", (message.chat.id, "name", "numb",))
        database.commit()
    else:
        pass


def add_user_name(message):
    cursor.execute("UPDATE user SET name=? WHERE id=?", (message.text, message.chat.id,))
    database.commit()


def add_user_numb(message):
    cursor.execute("UPDATE user SET numb=? WHERE id=?", (message.text, message.chat.id,))
    database.commit()


def delete_user(message):
    cursor.execute("DELETE FROM user WHERE 1=1")
    database.commit()


def inf(message):
    cursor.execute("SELECT name, numb FROM user")
    data = cursor.fetchall()
    database.commit()
    return data


def check_user(message):
    cursor.execute('SELECT user FROM name WHERE condition')
    data = cursor.fetchall()
    database.commit()
    return data












