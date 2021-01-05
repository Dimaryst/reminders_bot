import configparser as confp
import time
from datetime import date
import telebot
from telebot import types
from telegram_bot_calendar import DetailedTelegramCalendar, LSTEP
import modules

# Load Config
config = confp.ConfigParser()
config.read('config.ini')
tgToken = config["Variables"]["tlgrm_token"]
bot = telebot.TeleBot(tgToken)

print(f"Bot started at {time.ctime()}")


@bot.message_handler(commands=['start'])
def bot_intro(message):
    intro_message = config["BotPhrases"]["intro"]

    # Link in chat
    in_chat_markup = types.InlineKeyboardMarkup()
    myGitLinkInlineButton = types.InlineKeyboardButton(text='MyGit',
                                                       url='https://github.com/Dimaryst')
    in_chat_markup.add(myGitLinkInlineButton)
    modules.terminal_output(message)
    bot.send_message(message.chat.id,
                     intro_message + f"\nYour Telegram User ID: {message.from_user.id}",
                     reply_markup=in_chat_markup)

    # Buttons with commands
    func_markup = types.ReplyKeyboardMarkup()
    btn_CreateReminder = types.KeyboardButton('📝 Create new Reminder')
    btn_MyReminders = types.KeyboardButton('✏ Edit my Reminders')
    func_markup.row(btn_CreateReminder)
    func_markup.row(btn_MyReminders)
    if message.from_user.id == int(config["Users"]["dimaryst"]):
        bot.send_message(message.chat.id, "So... What we gonna do?", reply_markup=func_markup)
    else:
        bot.send_message(message.chat.id, "You are not allowed to work with this bot :(")


@bot.message_handler(content_types=['text'])
def bot_talks(message):
    if message.text == '📝 Create new Reminder' and message.from_user.id == int(config["Users"]["dimaryst"]):
        bot.send_message(message.chat.id, "Describe your reminder in a few words.")
        bot.register_next_step_handler(message, bot_request_date)
    elif message.text == '✏ Edit my Reminders' and message.from_user.id == int(config["Users"]["dimaryst"]):
        # bot.register_next_step_handler(message, edit_reminder.bot_send_list)
        print("Edit!")
    else:
        bot.send_message(message.chat.id, "I do not understand you."
                                          "\nPlease, use your special buttons.")


def bot_request_date(message):
    comment = message.text
    calendar, step = DetailedTelegramCalendar().build()
    bot.send_message(message.chat.id, f"Reminder: \"{comment}\"\nWhen would "
                                      "you like to receive a reminder "
                                      f"messages from me? Select {LSTEP[step]}:",
                     reply_markup=calendar)


@bot.callback_query_handler(func=DetailedTelegramCalendar.func())
def calFunc(c):
    #
    result, key, step = DetailedTelegramCalendar().process(c.data)
    if not result and key:
        bot.edit_message_text(f"Select {LSTEP[step]}:",
                              c.message.chat.id,
                              c.message.message_id,
                              reply_markup=key)
    elif result:
        bot.edit_message_text(f"You have scheduled notification on: {result}."
                              f"\nComment: ",
                              c.message.chat.id,
                              c.message.message_id)


bot.polling(none_stop=True)
