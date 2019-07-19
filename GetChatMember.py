#How To Work With GetChatMember in Python_Telegram_Bot


""" import"""
from telegram.ext import Updater, CommandHandler, Filters
ogging.basicConfig(level = logging.DEBUG,
                    format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger()
logger.setLevel(logging.INFO)



"""bot_token"""
updater = Updater("YOUR_TOKEN")



def GetChatMember(bot, update):

    var = bot.get_chat_member(chat_id = update.message.chat_id, user_id = update.message.from_user.id)
    print(var)



"""handlers"""
updater.dispatcher.add_handler(CommandHandler("start", GetChatMember))



updater.start_polling()
updater.idle()





result : 

{'user': {'id': ********, 'first_name': 'SOMTHING', 'is_bot': False, 'username': '*******', 'language_code': 'fa'}, 'status': 'creator', 'until_date': None}
