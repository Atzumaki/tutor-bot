import telebot
import os
import random
from telebot import types

bot = telebot.TeleBot('7717923468:AAHMyX8Jrv8XLOBNmBtlyYi69G4TjuvY8vc')

picture = os.listdir("Pictures")
adminids = []
answers = []
with open('AdminID', mode='r') as f:
    for _ in f.readlines():
        adminids.append(_[:-1])
with open('answer', encoding='utf-8') as file:
    for _ in file.readlines():
        answers.append(_[:-1])

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton('Профком')
    btn2 = types.KeyboardButton('МФСО')
    btn3 = types.KeyboardButton('Факультеты/институты')
    btn4 = types.KeyboardButton('Деканат')
    btn5 = types.KeyboardButton('Общежитие')
    btn6 = types.KeyboardButton('Стипендии')
    btn7 = types.KeyboardButton('ВУЦ')
    btn8 = types.KeyboardButton('Мотивация')
    btn9 = types.KeyboardButton('Вопрос админу')
    markup.row(btn1, btn2)
    markup.row(btn3, btn4)
    markup.row(btn5, btn6)
    markup.row(btn7, btn8)
    markup.row(btn9)
    bot.send_message(message.chat.id, 'Привет, я Тьютор-Бот, твой персональный помощник!', reply_markup=markup)
    bot.register_next_step_handler(message, on_click)


def adminIn(message, userid, adminid):
    msg = bot.send_message(adminid, f"Вопрос пользователя {message.text}")
    bot.register_next_step_handler(msg, adminOut, userid, adminid)

def adminOut(message1, userid, adminid):
    bot.send_message(userid, f"Ответ администратора: {message1.text}")

@bot.message_handler()
def on_click(message):
    if message.text == "Профком":
        section_1_menu(message)
    elif message.text == "МФСО":
        section_2_menu(message)
    elif message.text == "Факультеты/институты":
        section_1_menu(message)
    elif message.text == "Деканат":
        section_2_menu(message)
    elif message.text == "Общежитие":
        section_1_menu(message)
    elif message.text == "Стипендии":
        section_2_menu(message)
    elif message.text == "ВУЦ":
        section_1_menu(message)
    elif message.text == 'Мотивация':
        title = picture[random.randint(0, len(picture) - 1)]
        file = open(f'Picture/{title}', mode='rb')
        bot.send_photo(message.chat.id, file)
        file.close()
    elif message.text == 'Вопрос админу':
        bot.send_message(message.chat.id, 'Введите свой вопрос:')
        admin_id = adminids[random.randint(0, len(adminids) - 1)]
        bot.register_next_step_handler(message, adminIn, message.chat.id, admin_id)
    elif message.text == 'что такое профком?':
        bot.send_message(message.chat.id, answers[0])
    elif message.text == 'Что такое профсоюз?':
        bot.send_message(message.chat.id, answers[1])
    elif message.text == 'Что такое профбюро?':
        bot.send_message(message.chat.id, answers[2])
    elif message.text == 'Что такое МФСО?':
        bot.send_message(message.chat.id, answers[3])
    elif message.text == 'Где находится МФСО?':
        bot.send_message(message.chat.id, answers[4])
    elif message.text == 'Какой режим работы МФСО?':
        bot.send_message(message.chat.id, answers[5])

    else:
        print("Не пон")

# Раздел 1
def section_1_menu(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    # Кнопки для раздела 1
    btn1 = types.KeyboardButton("что такое профком?")
    btn2 = types.KeyboardButton("Что такое профсоюз?")
    btn3 = types.KeyboardButton("Что такое профбюро?")
    markup.add(btn1, btn2, btn3)
    bot.send_message(message.chat.id, "Вы в разделе Профсоюз", reply_markup=markup)

bot.polling(non_stop=True)