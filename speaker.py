from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters, RegexHandler,
                          ConversationHandler)

import subprocess

TOKEN = ''

def echo(bot,update):
    voice_file_id = update.message.voice.file_id
    print(voice_file_id)
    voice_file = bot.getFile(voice_file_id)
    voice_file.download('voice.ogg')
    update.message.reply_text('received!')
    subprocess.call(['opusdec voice.ogg voice.wav'],shell=True)
    subprocess.call(['aplay -Dplughw:CARD=Device voice.wav'], shell=True)

    



updater = Updater(TOKEN)
dp = updater.dispatcher
dp.add_handler(MessageHandler(Filters.voice,echo))


updater.start_polling()
updater.idle()
