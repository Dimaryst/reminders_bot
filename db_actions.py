import sqlite3


# Data Base with Reminders
# DB: reminders.db
# DB:
# Table with reminders: usrReminders
# Table with users: allowedUsers
def add_row(userid, date, time, comment):
    conn = sqlite3.connect('reminders.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM usrReminders ORDER BY rid DESC LIMIT 1;")
    result = cur.fetchone()
    newid = 0
    flag = 'in_progress'

    if result is not None:
        newid = int(result[0]) + 1

    data = [newid, userid, date, time, comment, flag]
    cur.execute("INSERT INTO usrReminders VALUES(?, ?, ?, ?, ?, ?);", data)
    conn.commit()
    return data


def del_row(rid):
    conn = sqlite3.connect('reminders.db')
    cur = conn.cursor()
    cur.execute(f"DELETE FROM usrReminders WHERE rid={rid};")
    conn.commit()


def check_user_reminders(userid):
    conn = sqlite3.connect('reminders.db')
    cur = conn.cursor()
    cur.execute(f"SELECT * FROM usrReminders WHERE userid={userid};")
    result = cur.fetchall()
    return result


def check_user(userid):
    conn = sqlite3.connect('reminders.db')
    cur = conn.cursor()
    cur.execute(f"SELECT * FROM allowedUsers WHERE userid={userid};")
    result = cur.fetchone()
    if result is not None:
        return True
    else:
        return False


def add_user(userid):
    conn = sqlite3.connect('reminders.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM allowedUsers ORDER BY id DESC LIMIT 1;")
    result = cur.fetchone()
    cur.execute("INSERT INTO allowedUsers VALUES(?, ?, ?);",
                [int(result[0]) + 1, userid, 100])
    conn.commit()

