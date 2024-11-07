import telebot
import os
import random
from telebot import types

bot = telebot.TeleBot('7717923468:AAHMyX8Jrv8XLOBNmBtlyYi69G4TjuvY8vc')

picture = os.listdir("Pictures")
adminids = []
answers = []
with open('AdminID.txt', mode='r') as f:
    for _ in f.readlines():
        adminids.append(_[:-1])
with open('answer.txt', encoding='utf-8') as file:
    for _ in file.readlines():
        answers.append(_[:-1])

@bot.message_handler(commands=['start'])
def start(message, *args):
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
    if args[0] != 1:
        bot.send_message(message.chat.id, 'Привет, я Тьютор-Бот, твой персональный помощник!', reply_markup=markup)
    else:
        bot.send_message(message.chat.id, 'Главное меню', reply_markup=markup)
    bot.register_next_step_handler(message, on_click)


def adminIn(message, userid, adminid):
    msg = bot.send_message(adminid, f"Вопрос пользователя {message.text}")
    bot.register_next_step_handler(msg, adminOut, userid, adminid)

def adminOut(message1, userid, adminid):
    bot.send_message(userid, f"Ответ администратора: {message1.text}")

@bot.message_handler()
def on_click(message):
    # $ это перенос на др строкув файле answer
    if message.text == "Профком":
        section_1_menu(message)
    elif message.text == "МФСО":
        section_2_menu(message)
    elif message.text == "Факультеты/институты":
        section_3_menu(message)
    elif message.text == "Деканат":
        section_4_menu(message)
    elif message.text == "Общежитие":
        section_5_menu(message)
    elif message.text == "Стипендии":
        section_6_menu(message)
    elif message.text == "ВУЦ":
        section_7_menu(message)
    elif message.text == 'Мотивация':
        title = picture[random.randint(0, len(picture) - 1)]
        file = open(f'Pictures/{title}', mode='rb')
        bot.send_photo(message.chat.id, file)
        file.close()
    elif message.text == 'Вопрос админу':
        bot.send_message(message.chat.id, 'Введите свой вопрос:')
        admin_id = adminids[random.randint(0, len(adminids) - 1)]
        bot.register_next_step_handler(message, adminIn, message.chat.id, admin_id)
    elif message.text == "Назад":
        start(message, 1)
    elif message.text == 'что такое профком?':
        answers[22] = answers[22].replace("$", "\n")
        bot.send_message(message.chat.id, answers[0])
    elif message.text == 'Что такое профсоюз?':
        answers[1] = answers[1].replace("$", "\n")
        bot.send_message(message.chat.id, answers[1])
    elif message.text == 'Что такое профбюро?':
        answers[2] = answers[2].replace("$", "\n")
        bot.send_message(message.chat.id, answers[2])
    elif message.text == 'Что такое МФСО?':
        answers[3] = answers[3].replace("$", "\n")
        bot.send_message(message.chat.id, answers[3])
    elif message.text == 'Где находится МФСО?':
        answers[4] = answers[4].replace("$", "\n")
        bot.send_message(message.chat.id, answers[4])
    elif message.text == 'Какой режим работы МФСО?':
        answers[5] = answers[5].replace("$", "\n")
        bot.send_message(message.chat.id, answers[5])
    elif message.text == 'ПИШ':
        answers[6] = answers[6].replace("$", "\n")
        bot.send_message(message.chat.id, answers[6])
    elif message.text == 'ФАДЭТ':
        answers[7] = answers[7].replace("$", "\n")
        bot.send_message(message.chat.id, answers[7])
    elif message.text == 'ФБФВИЖ':
        answers[8] = answers[8].replace("$", "\n")
        bot.send_message(message.chat.id, answers[8])
    elif message.text == 'ФПИК ПРИ УМПО':
        answers[9] = answers[9].replace("$", "\n")
        bot.send_message(message.chat.id, answers[9])
    elif message.text == 'ИГСН':
        answers[10] = answers[10].replace("$", "\n")
        bot.send_message(message.chat.id, answers[10])
    elif message.text == 'ИИМРТ':
        answers[11] = answers[11].replace("$", "\n")
        bot.send_message(message.chat.id, answers[11])
    elif message.text == 'ИИГУ':
        answers[12] = answers[12].replace("$", "\n")
        bot.send_message(message.chat.id, answers[12])
    elif message.text == 'ИП':
        answers[13] = answers[13].replace("$", "\n")
        bot.send_message(message.chat.id, answers[13])
    elif message.text == 'ИПЧ':
        answers[14] = answers[14].replace("$", "\n")
        bot.send_message(message.chat.id, answers[14])
    elif message.text == 'ИТМ':
        answers[15] = answers[15].replace("$", "\n")
        bot.send_message(message.chat.id, answers[15])
    elif message.text == 'ИХЗЧС':
        answers[16] = answers[16].replace("$", "\n")
        bot.send_message(message.chat.id, answers[16])
    elif message.text == 'ИНЭБ':
        answers[17] = answers[17].replace("$", "\n")
        bot.send_message(message.chat.id, answers[17])
    elif message.text == 'ИЭТИ':
        answers[18] = answers[18].replace("$", "\n")
        bot.send_message(message.chat.id, answers[18])
    elif message.text == 'ФТИ':
        answers[19] = answers[19].replace("$", "\n")
        bot.send_message(message.chat.id, answers[19])
    elif message.text == 'Что такое деканат?':
        answers[20] = answers[20].replace("$", "\n")
        bot.send_message(message.chat.id, answers[20])
    elif message.text == 'Какие функции у деканата?':
        answers[21] = answers[21].replace("$", "\n")
        bot.send_message(message.chat.id, answers[21])
    elif message.text == 'Как заселиться в общежитие?':
        answers[22] = answers[22].replace("$", "\n")
        bot.send_message(message.chat.id, answers[22])
    elif message.text == 'Студгородок №1':
        answers[23] = answers[23].replace("$", "\n")
        bot.send_message(message.chat.id, answers[23])
    elif message.text == 'Студгородок №2':
        answers[24] = answers[24].replace("$", "\n")
        bot.send_message(message.chat.id, answers[24])
    elif message.text == 'ГАС':
        answers[25] = answers[25].replace("$", "\n")
        bot.send_message(message.chat.id, answers[25])
    elif message.text == 'ГСС':
        answers[26] = answers[26].replace("$", "\n")
        bot.send_message(message.chat.id, answers[26])
    elif message.text == 'ПГАС':
        answers[27] = answers[27].replace("$", "\n")
        bot.send_message(message.chat.id, answers[27])
    elif message.text == 'Что такое ВУЦ?':
        answers[28] = answers[28].replace("$", "\n")
        bot.send_message(message.chat.id, answers[28])
    elif message.text == 'Программы военной подготовки':
        answers[29] = answers[29].replace("$", "\n")
        bot.send_message(message.chat.id, answers[29])
    else:
        print("Не пон")


# Раздел 1
def section_1_menu(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    # Кнопки для раздела 1
    btn1 = types.KeyboardButton("что такое профком?")
    btn2 = types.KeyboardButton("Что такое профсоюз?")
    btn3 = types.KeyboardButton("Что такое профбюро?")
    back_button = types.KeyboardButton("Назад")
    markup.add(btn1, btn2, btn3, back_button)
    bot.send_message(message.chat.id, "Вы в разделе Профсоюз", reply_markup=markup)


def section_2_menu(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn1 = types.KeyboardButton("Что такое МФСО?")
    btn2 = types.KeyboardButton("Где находится МФСО?")
    btn3 = types.KeyboardButton("Какой режим работы МФСО?")
    back_button = types.KeyboardButton("Назад")
    markup.add(btn1, btn2, btn3, back_button)
    bot.send_message(message.chat.id, "Вы в разделе МФСО", reply_markup=markup)


def section_3_menu(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn1 = types.KeyboardButton("ПИШ")
    btn2 = types.KeyboardButton("ФАДЭТ")
    btn3 = types.KeyboardButton("ФБФВИЖ")
    btn4 = types.KeyboardButton("ФПИК ПРИ УМПО")
    btn5 = types.KeyboardButton("ИГСН")
    btn6 = types.KeyboardButton("ИИМРТ")
    btn7 = types.KeyboardButton("ИИГУ")
    btn8 = types.KeyboardButton("ИП")
    btn9 = types.KeyboardButton("ИПЧ")
    btn10 = types.KeyboardButton("ИТМ")
    btn11 = types.KeyboardButton("ИХЗЧС")
    btn12 = types.KeyboardButton("ИНЭБ")
    btn13 = types.KeyboardButton("ИЭТИ")
    btn14 = types.KeyboardButton("ФТИ")
    back_button = types.KeyboardButton("Назад")
    markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9, btn10, btn11, btn12, btn13, btn14, back_button)
    bot.send_message(message.chat.id, "Вы в разделе МФСО", reply_markup=markup)


def section_4_menu(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn1 = types.KeyboardButton("Что такое деканат?")
    btn2 = types.KeyboardButton("Какие функции у деканата?")
    back_button = types.KeyboardButton("Назад")
    markup.add(btn1, btn2, back_button)
    bot.send_message(message.chat.id, "Вы в разделе Деканат", reply_markup=markup)


def section_5_menu(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn1 = types.KeyboardButton("Как заселиться в общежитие?")
    btn2 = types.KeyboardButton("Студгородок №1")
    btn3 = types.KeyboardButton("Студгородок №2")
    back_button = types.KeyboardButton("Назад")
    markup.add(btn1, btn2, btn3, back_button)
    bot.send_message(message.chat.id, "Вы в разделе Общежитие", reply_markup=markup)


def section_6_menu(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn1 = types.KeyboardButton("ГАС")
    btn2 = types.KeyboardButton("ГСС")
    btn3 = types.KeyboardButton("ПГАС")
    back_button = types.KeyboardButton("Назад")
    markup.add(btn1, btn2, btn3, back_button)
    bot.send_message(message.chat.id, "Вы в разделе Стипендии", reply_markup=markup)


def section_7_menu(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn1 = types.KeyboardButton("Что такое ВУЦ?")
    btn2 = types.KeyboardButton("Программы военной подготовки")
    back_button = types.KeyboardButton("Назад")
    markup.add(btn1, btn2, back_button)
    bot.send_message(message.chat.id, "Вы в разделе ВУЦ", reply_markup=markup)


bot.polling(non_stop=True)
