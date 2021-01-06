from telebot import types
import MyBot
from MyBot import bot
import db_actions


def add_new_reminder(message):
    bot.send_message(message.chat.id, "Describe you reminder:"
                                      "\n(month-day hour-minute \"your comment\")"
                                      "\nExample: 11-03 23-00 Destroy the Galaxy!")
    bot.register_next_step_handler(message, write_reminder)


def write_reminder(message):
    btns = types.ReplyKeyboardMarkup()
    btns.row(types.KeyboardButton(MyBot.gtMainMenu_btn))
    btns.row(types.KeyboardButton(MyBot.myRem_btn))
    raw_reminder = message.text
    reminder = raw_reminder.split(" ", 2)
    re = db_actions.add_row(message.from_user.id, reminder[0], reminder[1], reminder[2])
    bot.send_message(message.chat.id, f"Done! Committed Data:"
                                      f"\n{re}",
                     reply_markup=btns)
