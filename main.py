import time
from telebot import types
import db_actions
import add_reminder
import edit_reminders
import MyBot
from MyBot import bot

print(f"Bot started at {time.ctime()}")


@bot.message_handler(commands=['start'])
def bot_intro(message):
    intro_message = "Hi! I'm your personal reminder, " \
                    "so if you want me to remind you about something important, " \
                    "check buttons below. Enjoy!"

    # Link in chat
    in_chat_markup = types.InlineKeyboardMarkup()
    myGitLinkInlineButton = types.InlineKeyboardButton(text='MyGit',
                                                       url='https://github.com/Dimaryst')
    in_chat_markup.add(myGitLinkInlineButton)
    bot.send_message(message.chat.id,
                     intro_message + f"\nYour Telegram User ID: {message.from_user.id}",
                     reply_markup=in_chat_markup)
    if db_actions.check_user(message.from_user.id):
        bot_main_menu(message)


@bot.message_handler(content_types=['text'])
def bot_talks(message):
    if message.text == MyBot.gtMainMenu_btn:
        bot_main_menu(message)
    elif message.text == MyBot.newRem_btn:
        add_reminder.add_new_reminder(message)
    elif message.text == MyBot.myRem_btn:
        edit_reminders.show_my_reminders(message)
    else:
        bot.send_message(message.chat.id, "I do not understand you."
                                          "\nPlease, use your special buttons.")


@bot.message_handler(commands=['main'])
def bot_main_menu(message):
    # Buttons with commands
    func_markup = types.ReplyKeyboardMarkup()
    btn_CreateReminder = types.KeyboardButton(MyBot.newRem_btn)
    btn_MyReminders = types.KeyboardButton(MyBot.myRem_btn)
    func_markup.row(btn_CreateReminder)
    func_markup.row(btn_MyReminders)
    bot.send_message(message.chat.id, "Main menu.\nSo... What we gonna do?", reply_markup=func_markup)


bot.polling(none_stop=True)
