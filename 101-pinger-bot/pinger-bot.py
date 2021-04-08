import settings
import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

import sys
from pythonping import ping


logging.basicConfig(filename='bot.log', level=logging.INFO)

def main():
    mybot = Updater(settings.API_KEY, use_context=True)
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    logging.info("Бот стартовал")
    mybot.start_polling()
    mybot.idle()

def greet_user(update, context):
    update.message.reply_text('Бот стартовал! Ты вызвал команду /start')

def talk_to_me(update, context):
    ip_addr = update.message.text
    print(ip_addr)
    result = sys.stdout
    response_list = ping(ip_addr, verbose=True)
    update.message.reply_text(result)

if __name__ == "__main__":
    main()