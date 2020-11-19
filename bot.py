# -*- coding: utf-8 -*- 
import telebot
from telebot import TeleBot
import logging
import requests
from time import sleep
from PIL import Image 

TOKEN = 'ur_token_here'


types = telebot.types
bot = TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def handle_grammar2(m):
    bot.send_message(m.from_user.id, f"<b>Добро пожаловать, {m.from_user.first_name}</b>", parse_mode='HTML', disable_notification=True)
    sleep(0.01)


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
 chat_id = int(message.chat.id)
 text = message.text
 
 if message.text == u'/wallpaper':
      url = 'https://nekos.life/api/v2/img/wallpaper'
      r = requests.get(url, allow_redirects=True)
      r.headers
      json = r.json()
      pussyurl = json['url']
      rs = requests.get(pussyurl, allow_redirects=True)
      open('wallpaper.png', 'wb').write(rs.content)
      print("Обои отправленны!")
      bot.send_photo(message.chat.id, open("wallpaper.png", "rb"), disable_notification=True)
      sleep(3)
      bot.send_document(message.chat.id, open("wallpaper.png","rb"), disable_notification=True)
      sleep(3)
      bot.send_message(message.chat.id, f"<b>Обои можно запрашивать раз в 10 секунд!</b>", parse_mode='HTML', disable_notification=True)
      sleep(10)
                     

bot.polling(none_stop=True, interval=0)
