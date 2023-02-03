import os
import telebot
import os.path

API_TOKEN = '5797067852:AAH64nToAYrdRYMFznVFiLUdcPYRwLq5BRM'

bot = telebot.TeleBot(API_TOKEN)
file_path_for_edit = 'test.txt'
checkFile = os.path.exists(file_path_for_edit)


@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, 'Заменяю з на Z')


# @bot.message_handler(func=lambda message: True)
# def echo_message(message):
#     bot.reply_to(message, message.text)

@bot.message_handler(content_types=['text'])
def send_welcome(message):
    if message.text == '/reg':
        bot.send_message(message.chat.id, "Пришлите текст")
        bot.register_next_step_handler(message, text_filter)
    else:
        bot.send_message(message.chat.id, 'Напиши /reg');

# def edit_word(message):
#
#     bot.register_next_step_handler(message, text_filter)


def text_filter(message):
    if checkFile:
        with open(file_path_for_edit, 'w') as f:
            f.write(message)

    # else:
    #     with open(file_path_for_edit, 'w') as f:
    #         f.write(message)
    with open('test.txt', 'r') as f:
        context = f.read()
        filter_ = context.replace('з', 'Z')
        # my_file = open(file_path_for_edit, "w+")

    with open('createfile.txt', 'w') as f:
        f.write(filter_)

        with open('createfile.txt', 'r') as file:
            print(file.read())

        fileCreate = 'createfile.txt'

    with open('createfile.txt', 'r') as f:
        w = f

    bot.send_message(message.chat.id, w)

    os.remove(fileCreate)


bot.infinity_polling()
