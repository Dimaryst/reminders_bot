from telebot import types
import MyBot
from MyBot import bot
import db_actions

REQUEST = []


def show_my_reminders(message):
    user_reminders = db_actions.check_user_reminders(userid=message.from_user.id)
    btns = types.ReplyKeyboardMarkup()
    if str(user_reminders).find("in_progress") != -1:
        for itm in user_reminders:
            btnText = f"{str(itm[0])} // \"{str(itm[4])}\" -- {str(itm[2])}/{str(itm[3])}"
            btns.row(types.KeyboardButton(btnText))
        bot.send_message(message.chat.id,
                         f"Select the reminder that you want to modify:",
                         reply_markup=btns)
        bot.register_next_step_handler(message, edit_selected_reminder)
    else:
        btns.row(types.KeyboardButton(MyBot.newRem_btn))
        btns.row(types.KeyboardButton(MyBot.gtMainMenu_btn))
        bot.send_message(message.chat.id, f"Reminders list is empty.", reply_markup=btns)


def edit_selected_reminder(message):
    REQUEST.append(message.text.split(" ", 1)[0])  #
    btns = types.ReplyKeyboardMarkup()
    btns.row(types.KeyboardButton(MyBot.del_btn))
    btns.row(types.KeyboardButton(MyBot.mdfy_btn))
    btns.row(types.KeyboardButton(MyBot.myRem_btn))
    btns.row(types.KeyboardButton(MyBot.gtMainMenu_btn))
    bot.send_message(message.chat.id, f"Selected reminder:"
                                      f"\n{message.text}"
                                      f"\n\nOkay, what do you want to do with it?",
                     reply_markup=btns)

    bot.register_next_step_handler(message, write_changes)


def write_changes(message):
    REQUEST.append(message.text)
    btns = types.ReplyKeyboardMarkup()
    btns.row(types.KeyboardButton(MyBot.myRem_btn))
    btns.row(types.KeyboardButton(MyBot.gtMainMenu_btn))
    if message.text == MyBot.del_btn:
        db_actions.del_row(REQUEST[0])
        bot.send_message(message.chat.id,
                         f"Reminder deleted.",
                         reply_markup=btns)
    elif message.text == MyBot.mdfy_btn:
        bot.send_message(bot.send_message(message.chat.id,
                                          f"This function doesn't work",
                                          reply_markup=btns))
    REQUEST.clear()
    print(REQUEST)
