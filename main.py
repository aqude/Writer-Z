import os
import telebot
import os.path

API_TOKEN = '5797067852:AAH64nToAYrdRYMFznVFiLUdcPYRwLq5BRM'

bot = telebot.TeleBot(API_TOKEN)

# файл для чтения
file_path_for_edit = 'test.txt'
checkFile = os.path.exists(file_path_for_edit)

# файл для записи и удаления
fileCreate = 'createfile.txt'


@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, 'Заменяю з на Z')


# @bot.message_handler(func=lambda message: True)
# def echo_message(message):
#     bot.reply_to(message, message.text)

@bot.message_handler(content_types=['text'])
def send_welcome(message):
    if message.text == '/z':
        msg_user = bot.send_message(message.user.id, "Пришлите текст")
        bot.register_next_step_handler(msg_user, text_filter)
    else:
        bot.send_message(message.user.id, 'Напиши /z')


# def edit_word(message):
#
#     bot.register_next_step_handler(message, text_filter)


def text_filter(message):
    if checkFile:
        with open(file_path_for_edit, 'w+') as f:
            f.write(message.text)
    else:
        print("not found file")

    # else:
    #     with open(file_path_for_edit, 'w') as f:
    #         f.write(message)
    with open(file_path_for_edit, 'r') as f:
        context = f.read()
        filter_ = context.replace('з', 'Z')
        # my_file = open(file_path_for_edit, "w+")

    with open(fileCreate, 'w') as f:
        f.write(filter_)

    with open(fileCreate, 'r') as file:
        data = file.read().replace('\n', '')

    with open('createfile.txt', 'r') as f:
        w = f.read()

    bot.send_message(message.user.id, w)

    # удаляем файл
    os.remove(fileCreate)
    # отчищаем файл
    with open(file_path_for_edit, 'w') as f:
        f.write('')


bot.infinity_polling()
