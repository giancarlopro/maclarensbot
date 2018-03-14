import os
from telegram.ext import Updater, CommandHandler

token = os.environ.get("TOKEN")
port = int(os.environ.get('PORT', '443'))

def saymyname (bot, update):
    update.message.reply_text(update.message.from_user.first_name)

updater = Updater(token)

updater.dispatcher.add_handler(CommandHandler('/saymyname', saymyname))

updater.start_webhook(listen="0.0.0.0", port=port, url_path=token)
updater.bot.set_webhook("https://maclarensbot.herokuapp.com/" + token)
updater.idle()