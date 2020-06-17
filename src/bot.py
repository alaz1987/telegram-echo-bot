import telebot
import config
from telebot import apihelper

apihelper.proxy = {'https':'socks5h://localhost:9150'}

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(content_types = ["text"])

def send(message):
    bot.send_message(message.chat.id, message.text)

# RUN
bot.polling(none_stop = True)