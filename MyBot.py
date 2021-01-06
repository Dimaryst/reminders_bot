import telebot
import configparser as confp

config = confp.ConfigParser()
config.read('config.ini')
tgToken = config["Variables"]["tlgrm_token"]

bot = telebot.TeleBot(tgToken)
gtMainMenu_btn = "Go to Main Menu"
newRem_btn = "Create new Reminder"
myRem_btn = "My Reminders"

mdfy_btn = "Modify"
del_btn = "Delete"
