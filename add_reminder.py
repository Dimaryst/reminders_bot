from telebot import types
import MyBot
from MyBot import bot
import db_actions


def add_new_reminder(message):
    btns = types.ReplyKeyboardMarkup()
    btns.row(types.KeyboardButton(MyBot.abort_btn))
    bot.send_message(message.chat.id, "Describe you reminder:"
                                      "\n(month-day hour-minute \"your comment\")"
                                      "\nExample: 11-03 23-00 Destroy the Galaxy!",
                     reply_markup=btns)
    bot.register_next_step_handler(message, write_reminder)


def write_reminder(message):  # TODO: Template for input string
    reminder_str = message.text.strip()
    btns = types.ReplyKeyboardMarkup()
    btns.row(types.KeyboardButton(MyBot.myRem_btn))
    btns.row(types.KeyboardButton(MyBot.newRem_btn))
    if message.text == MyBot.abort_btn:
        abort_action(message)
    elif len(reminder_str) < 13 \
            or reminder_str.count(" ") < 2 \
            or reminder_str[0] == " ":
        bot.send_message(message.chat.id, "Incorrect parameters", reply_markup=btns)
    else:
        reminder = reminder_str.split(" ", 2)
        re = str(db_actions.add_row(message.from_user.id,
                                    reminder[0], reminder[1], reminder[2]))
        bot.send_message(message.chat.id, f"Done!"
                                          f"\nCommitted Data:"
                                          f"\n{re}",
                         reply_markup=btns)


def abort_action(message):
    btns = types.ReplyKeyboardMarkup()
    btns.row(types.KeyboardButton(MyBot.gtMainMenu_btn))
    btns.row(types.KeyboardButton(MyBot.myRem_btn))
    bot.send_message(message.chat.id, "Canceled", reply_markup=btns)
