import telebot
import os
import random
from telebot import types

bot = telebot.TeleBot('7717923468:AAHMyX8Jrv8XLOBNmBtlyYi69G4TjuvY8vc')
global picture
picture = os.listdir("Picture")
global adminids
adminids = []
with open('AdminID', mode='r') as f:
    for _ in f.readlines():
        adminids.append(_[:-1])

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton('Профком')
    btn2 = types.KeyboardButton('МФСО')
    btn3 = types.KeyboardButton('Деканат')
    btn4 = types.KeyboardButton('Социальная работа')
    btn5 = types.KeyboardButton('Общежитие')
    btn6 = types.KeyboardButton('Международное сотрудничество')
    btn7 = types.KeyboardButton('Стипендии')
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
    if message.text == 'Мотивация':
        title = picture[random.randint(0, len(picture) - 1)]
        file = open(f'Picture/{title}', mode='rb')
        bot.send_photo(message.chat.id, file)
        file.close()
    elif message.text == 'Вопрос админу':
        bot.send_message(message.chat.id, 'Введите свой вопрос:')
        # admin_id = adminids[random.randint(0, len(adminids) - 1)]
        admin_id = 1447192776
        bot.register_next_step_handler(message, adminIn, message.chat.id, admin_id)
    else:
        if message.chat.id in adminids:
            pass
        else:
            bot.send_message(message.chat.id, 'Кринж несёшь милая, я не понял')


bot.polling(non_stop=True)