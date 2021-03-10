import os
import json
import random

from flask import Flask, request

from telegram.ext import CommandHandler, Dispatcher
from telegram import Bot, Update

from . naointendo import NaoIntendo
from . search import GoogleSearch
from . topics import Topic

app = Flask(__name__)

token = os.environ.get('TOKEN')
port = int(os.environ.get('PORT', '443'))
status_ok = '{"status": "OK"}'
maclarenspub_id = '-1001240676821'

def saymyname(bot, update):
    update.message.reply_text('Heisenberg')

def naointendo(bot, update = None, chat_id = None):
    ni = NaoIntendo()
    post = ni.random_post()
    caption = "{title}\n--\n{desc}".format(title=post['title'], desc=post['desc'])

    if not chat_id:
        chat_id = update.message.chat.id

    if post['img'][-4:] == '.gif':
        bot.sendDocument(chat_id=chat_id, document=post['img'], caption=caption)
    else:
        bot.sendPhoto(chat_id=chat_id, photo=post['img'], caption=caption)

def redhead(bot, update = None, chat_id = None):
    gs = GoogleSearch()
    redhead_url = gs.random_redhead()

    if not chat_id:
        chat_id = update.message.chat.id

    bot.sendPhoto(chat_id=chat_id, photo=redhead_url)

def debug (bot, update):
    update.message.reply_text(update.message.chat_id)

def randompic(bot, update = None, chat_id = None, args = None):
    gs = GoogleSearch()

    global topics

    if args:
        query = ' '.join(args)
    else:
        query = Topic.random()
    
    if not chat_id:
        chat_id = update.message.chat.id

    random_url = gs.random_image(query)

    bot.sendPhoto(chat_id=chat_id, photo=random_url)

def setup():
    global token
    bot = Bot(token)
    
    dispatcher = Dispatcher(bot, None, workers=0)

    dispatcher.add_handler(CommandHandler('saymyname', saymyname))
    dispatcher.add_handler(CommandHandler('naointendo', naointendo))
    dispatcher.add_handler(CommandHandler('debug', debug))
    dispatcher.add_handler(CommandHandler('redhead', redhead))
    dispatcher.add_handler(CommandHandler('randompic', randompic, pass_args=True))

    # bot.set_webhook("https://maclarensbot.herokuapp.com/" + token)
    return dispatcher

@app.route("/send/joninhas")
def send_joninhas ():
    global token
    bot = Bot(token)

    global maclarenspub_id

    bot.sendMessage(
        chat_id=maclarenspub_id,
        text="It's time for *Joninhas*",
        parse_mode='Markdown'
    )
    bot.sendSticker(chat_id=maclarenspub_id, sticker="CAADAQADCQADEcFSHDYMLlVh2wPKAg")

    global status_ok
    return status_ok

@app.route("/send/naointendo")
def send_naointendo ():
    global token
    bot = Bot(token)

    global maclarenspub_id
    naointendo(bot, chat_id=maclarenspub_id)

    global status_ok
    return status_ok

@app.route('/' + str(token), methods=['GET', 'POST'])
def webhook ():
    global token
    bot = Bot(token)

    dispatcher = setup()

    text = request.data

    update = Update.de_json(json.loads(text), bot)

    dispatcher.process_update(update)

    global status_ok
    return status_ok

@app.route('/')
def wellcome ():
    global status_ok
    return status_ok

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)