# -*- coding: utf-8 -*-
import config
import telebot
from telebot import types

bot = telebot.TeleBot(config.token)



@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, 'Привет!')

# @bot.message_handler(content_types=['photo', 'document', 'audio', 'video'])
# def all_media_messages(message):
#     if message.caption is not None:
#         bot.forward_message(config.wheretosend_chatid, message.chat.id, message.message_id)

@bot.message_handler(content_types=['text'])
def send_text(message):
    for chat_id in config.CHAT_IDS:
        if message.text is not None:
            bot.send_message(config.wheretosend_chatid, message.text)


# @bot.message_handler(content_types=['attachment'])
# def send_document(message):
#     if message.document is not None:
#         bot.send_document(config.wheretosend_chatid, message.attachment)

# @bot.message_handler(func=lambda message: True, content_types=['photo'])
# def send_photo(message):
#     if message.photo is not None:
#         for photo in message.photo:
#             bot.send_message(config.wheretosend_chatid, photo)

# @bot.message_handler(content_types=['audio'])
# def send_audio(message):
#     if message.audio is not None:
#         bot.send_audio(config.wheretosend_chatid, audio)
        
@bot.message_handler(content_types=['photo', 'text'])
def all_media_messages(message):
    for chat_id in config.CHAT_IDS:
        if message.photo:
            photo = message.photo[-1]
            file_id = photo.file_id
            file_info = bot.get_file(file_id)
            downloaded_file = bot.download_file(file_info.file_path)
            bot.send_photo(config.wheretosend_chatid, downloaded_file, caption=message.caption)

bot.polling(none_stop=True)





