import os
import telebot
import random
import answers


API_KEY = os.environ['apikey']
bot = telebot.TeleBot(API_KEY)
text = ""

@bot.message_handler(commands=['help', "start"])
def help(message):
  text = open("help.txt","r")
  bot.reply_to(message, text)

@bot.message_handler(commands=["commands"])
def commandsfun(message):
  text = open("commands.txt","r")
  bot.reply_to(message, text.read())

@bot.message_handler(regexp='discopino')
@bot.message_handler(regexp='pino')
def pino(message):
  bot.send_message(message.chat.id, random.choice(answers.pinoar))


@bot.message_handler(regexp='muori')
@bot.message_handler(regexp='morite')
@bot.message_handler(regexp='morte')

def muori(message):
  bot.send_message(message.chat.id, random.choice(answers.muori))


@bot.message_handler(regexp='marijuana')
@bot.message_handler(regexp='droga')
def tony(message):
  bot.send_message(message.chat.id, random.choice(answers.droga))


@bot.message_handler(regexp='coki')
@bot.message_handler(regexp='coghi')
@bot.message_handler(regexp='koghy')
@bot.message_handler(regexp='cookie')
@bot.message_handler(regexp='koghi')
@bot.message_handler(regexp='ikoc')
@bot.message_handler(regexp='icok')
def coki(message):
  bot.send_message(message.chat.id, random.choice(answers.coki))

@bot.message_handler(regexp='strunz')
bot.polling()