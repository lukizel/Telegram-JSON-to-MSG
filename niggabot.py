#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import json
import requests

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)



def gen(update, context):
    r = requests.get('https://accgen.cathook.club/api/v1/account/FC2C8TW-3KM4DE9-JY15SVX-KRP5PTQ')
    update.message.reply_text(r.json())


def help(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text('/gen - generates a new steam account')

def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater("862997460:AAES_yIgOKuTLJY42C0_Jg4yxbGUq-TPCLs", use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("gen", gen))
    dp.add_handler(CommandHandler("help", help))
    
    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
