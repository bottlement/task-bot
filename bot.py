import telebot
#from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler, CallbackQueryHandler

Token ="6692242871:AAEpSdeLg_qKAwvw5hsm0oUqhVvkG1l8QiI"
bot = telebot.TeleBot(Token)

@bot.message_handler(["start"])
def start (message):
    bot.reply_to(message,"Welcome to Nitra campus bot")

# Responses
'''@bot.message_response(["response"])
def message_response (text):
    bot.reply_to(text)

    if "hello "in text :
        return "hey there!"
    
    if "how are you "in text:
        return " I am good !"
    if "I love Python "in text:
        return "Remember to Subscribe it!" 


    return " I do not understand what you are wrote.....?" '''


@bot.message_handler(["help"])
def help (message):
    bot.reply_to(message,"""
/start -> Hello ! thanks for chatting  with me!  I am Ntc Bot!
/help -> I Will give you all Commands  Lists, It will help about the Nitra Campus
/update -> I am ntc bot ! Please type  something so I Can Respond!    
 
    """)


"""@bot.message_handler(["text"])
def text (message):
        bot.reply_to(message,
      try:  
        if"hii " in text :
            return "hellow" 
      
        if "hello "in text :
            return "hey there!"
       )"""
    



@bot.message_handler()
def custom(message):
    try: 
        msg = eval(message.text.strip())
    except Exception as e:
        msg = "Sorry ! I can't understand,  Something Went worng .... "

    bot.reply_to (message,msg)
'''
@bot.message_handler()
def echo_all(message):
    
'''


bot.polling()