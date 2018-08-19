import os
import json
from flask import Flask, request
from telegram.ext import CommandHandler, Dispatcher
from telegram import Bot, Update

from naointendo import NaoIntendo
from search import GoogleSearch

app = Flask(__name__)

token = os.environ.get("TOKEN")
port = int(os.environ.get('PORT', '443'))

def saymyname(bot, update):
    update.message.reply_text("Heisenberg")

def naointendo(bot, update):
    ni = NaoIntendo()
    post = ni.random_post()
    caption = '''
        {title}
        --
        {desc}
    '''.format(title=post['title'], desc=post['desc'])
    if post['img'][-4:] == '.gif':
        bot.sendDocument(chat_id=update.message.chat.id, document=post['img'], caption=caption)
    else:
        bot.sendPhoto(chat_id=update.message.chat.id, photo=post['img'], caption=caption)
    # update.message.reply_text(ni.random_post())

def redhead(bot, update):
    gs = GoogleSearch()
    rh = gs.random_redhead()
    bot.sendPhoto(chat_id=update.message.chat.id, photo=rh, caption='By @{}'.format(update.effective_user.username))

def debug (bot, update):
    update.message.reply_text(update.message.chat_id)

def setup():
    global token
    bot = Bot(token)
    
    dispatcher = Dispatcher(bot, None, workers=0)
    dispatcher.add_handler(CommandHandler('saymyname', saymyname))
    dispatcher.add_handler(CommandHandler('naointendo', naointendo))
    dispatcher.add_handler(CommandHandler('debug', debug))
    dispatcher.add_handler(CommandHandler('redhead', redhead))

    # bot.set_webhook("https://maclarensbot.herokuapp.com/" + token)
    return dispatcher

@app.route("/HKMLFFGP/sendjoninhas")
def sendjoninhas ():
    global token
    bot = Bot(token)

    maclarens_id = "-1001240676821"

    bot.sendMessage(chat_id=maclarens_id, text="It's time for *Joninhas*", parse_mode='Markdown')
    bot.sendSticker(chat_id=maclarens_id, sticker="CAADAQADCQADEcFSHDYMLlVh2wPKAg")
    return "Ok"

@app.route("/sni")
def sendnaointendo ():
    global token
    bot = Bot(token)

    maclarens_id = "-1001240676821"
    ni = NaoIntendo()
    post = ni.random_post()

    caption = '''
        {title}
        --
        {desc}
    '''.format(title=post['title'], desc=post['desc'])
    
    if post['img'][-4:] == '.gif':
        bot.sendDocument(chat_id=maclarens_id, document=post['img'], caption=caption)
    else:
        bot.sendPhoto(chat_id=maclarens_id, photo=post['img'], caption=caption)
    
    return 'Worked!'

@app.route('/' + str(token), methods=['GET', 'POST'])
def webhook ():
    global token
    bot = Bot(token)

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