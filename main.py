from telebot import TeleBot
from config import TOKEN

bot = TeleBot(TOKEN)

@bot.message_handler(content_types=['text'])
def welcome(message):
    bot.reply_to(message, message)

if __name__=="__main__":
    bot.polling()