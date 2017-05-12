# coding=utf-8

from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters
import random

# Setiar el token del bot en el updater
# Set the bot's token
updater = Updater(token='TOKEN')
dispatcher = updater.dispatcher

# Respuestas que quiere que el bot de
# Answers List
listaRespuestas = ["RESPUESTAS"]

# Palabras a las que el bot va a reaccionar
# Words that will trigger the bot
menciones = ["Hi","No","Yes","Oui"]

# convertir a unicode - Convert to unicode
listaMenciones = [i.decode('UTF-8') if isinstance(i, basestring) else i for i in menciones]


# Funciones.
def test(bot, update):
	bot.sendMessage(chat_id=update.message.chat_id, 
		text="Bip bup bop... Funcionando!!!")


def reply(bot, update):
    try:
    	# Obtengo el texto que mandaron
        # Get the text the user sent
        text = update.message.text
        print (text)
        
        if any(x in text for x in listaMenciones):
        	# Enviar respuesta
	      	# Send back the result
	        bot.sendMessage(chat_id=update.message.chat_id,
	        text=random.choice (listaRespuestas))
	    
    except UnicodeEncodeError:
        bot.sendMessage(chat_id=update.message.chat_id, 
        text="Error")

# Con los CommandHandler se llaman los comandos con "/"
# CommandHanlder will react to words that begins with "/"
start_handler = CommandHandler('test', test)

# Con los MessageHandler recibe todo lo que se escribe.
# With MessageHandler the bot will receive all the text.
reply_handler = MessageHandler([Filters.text], reply)

# Agregar los handlers al dispatcher
# Add handlers to dispatcher
dispatcher.add_handler(test_handler)
dispatcher.add_handler(reply_handler)

updater.start_polling()