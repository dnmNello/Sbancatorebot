import os
import telebot
import random
import answers


#API_KEY = os.environ['apikey']
API_KEY = 5283104370:AAFo2wPFjHtV_a5XLjaicencTCCP2QC9QMc
bot = telebot.TeleBot(API_KEY)
text = ""

@bot.message_handler(commands=['help', "start"])
def help(message):
  text = open("help.txt","r") 
  bot.reply_to(message, text.read())

@bot.message_handler(regexp='ragazza')
@bot.message_handler(regexp='ragazze')
@bot.message_handler(regexp='ideale')
def rgzee(message):
  text = open("rgze.txt","r") 
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
def droga(message):
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
def coki(message):
    bot.send_message(message.chat.id,  random.choice(answers.strunz))
bot.polling()
