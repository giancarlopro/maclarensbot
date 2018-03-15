import os
from flask import Flask
from telegram.ext import CommandHandler, Dispatcher
from telegram import Bot, Update

app = Flask(__name__)

token = os.environ.get("TOKEN")
port = int(os.environ.get('PORT', '443'))

def saymyname (bot, update):
    update.message.reply_text(update.message.from_user.first_name)

def setup():
    global token
    bot = Bot(token)
    
    dispatcher = Dispatcher(bot, None, workers=0)
    dispatcher.add_handler(CommandHandler('saymyname', saymyname))

    bot.set_webhook("https://maclarensbot.herokuapp.com/" + token)
    return dispatcher

@app.route('/' + str(token), methods=['GET', 'POST'])
def webhook ():
    dispatcher = setup()

    text = request.data

    update = Update.de_json(json.loads(text), bot)

    dispatcher.process_update(update)
    return "Ok"

@app.route('/')
def wellcome ():
    return "OK"

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)