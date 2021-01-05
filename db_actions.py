import sqlite3

# Data Base with Reminders
# DB: reminders.db
# Table: usrReminders
conn = sqlite3.connect('reminders.db')
cur = conn.cursor()

currentReminderRequest = ('12', '384037601', 'reminfo', 'remdate', 'remflag')


# cur.execute("INSERT INTO usrReminders VALUES(?, ?, ?, ?, ?);", currentReminderRequest)
# conn.commit()

def Add_row(userid, comment, date):
    cur.execute("SELECT * FROM usrReminders ORDER BY remid DESC LIMIT 1;")
    result = cur.fetchone()
    newid = int(result[0]) + 1


Add_row()
