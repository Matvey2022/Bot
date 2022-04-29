from email import message
from setuptools import Command
import telebot
bot = telebot.TeleBot ( "5383758988:AAG-XTVK3fzCrQ0GE2kTE76vMKllg0dvc_Q", parse_mode=None )
@bot.massage_handler(command = ['start'])
def  send_welcom(message):
        bot.reply_to(message,'''hi''')