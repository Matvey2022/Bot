from ctypes import resize
from email import message
from gc import callbacks
from tkinter import Button
from tracemalloc import start
import types
from setuptools import Command
import telebot
bot = telebot.TeleBot ( "5383758988:AAG-XTVK3fzCrQ0GE2kTE76vMKllg0dvc_Q", parse_mode=None )
@bot.message_handler(command=[start])
def first(message):
    markup_inline = types.InlineKeyboardMarkup()
    iteam_1 = types.InlineKeyboardButton(text='Девушки',callback_data ='1')
    iteam_2 = types.InlineKeyboardButton(text='Услуги Взлома',callback_data ='2')
    iteam_3 = types.InlineKeyboardButton(text='Закрыть займы',callback_data ='3')
    iteam_4 = types.InlineKeyboardButton(text='Личный кабинет',callback_data ='4')
    iteam_5 = types.InlineKeyboardButton(text='Пополнить',callback_data ='5')

    markup_inline.add(iteam_1,iteam_2,iteam_3,iteam_4,iteam_5)
    bot.send_message(message.chat.id,'''Привет!👋🏻
                                        В этом боте ты можешь выбрать любую девушку на свой вкус
                                        для живого общения!👩‍❤️‍👨 ''',
        reply_markup=markup_inline
    )

@bot.callback_query_handler(func=lambda call: True)
def answer(call):
    if call.data == '1':
        markup_reply = types.ReplyKeyboardMarkup(resize_keyboard = True)
        iteam_a = types.KeyboardButton('Лера...')
    elif call.data == '2':
        markup_reply = types.ReplyKeyboardMarkup(resize_keyboard = True)
        iteam_b = types.KeyboardButton('КТО ТО...') 
    elif call.data == '3':
        markup_reply = types.ReplyKeyboardMarkup(resize_keyboard = True)
        iteam_c = types.KeyboardButton('ХТО ТО...') 
    elif call.data == '4':
        markup_reply = types.ReplyKeyboardMarkup(resize_keyboard = True)
        iteam_d = types.KeyboardButton('нехта...') 
    elif call.data == '5':
        markup_reply = types.ReplyKeyboardMarkup(resize_keyboard = True)
        iteam_f = types.KeyboardButton('Vjnz...') 
    

        markup_reply.add(iteam_a,iteam_b,iteam_c,iteam_d,iteam_f )
        bot.send_message(call.message.chat.id,'''Просмотр категорий''',
            reply_markup=markup_reply
        )


bot.infinity_polling()    