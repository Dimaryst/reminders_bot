import configparser as confp
import telebot
from telebot import types


# print info about incoming message
def terminal_output(message):
    print(f"User: \n{message.from_user}\n"
          f"Message: {message.text}\n\n")
