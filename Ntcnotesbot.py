import telebot

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
    if " Good Morning " in text :
        return " Very Good Morning " 
    else:
    
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
        if "hello "in text :
            return "hey there!"
        
        if "how are you "in text:
            return " I am good !"
        if "I love Python "in text:
            return "Remember to Subscribe it!" 

    except Exception as e:
        return " I do not understand what you are wrote.....?
    bot.reply_to =(message)

    """
    



@bot.message_handler()
def custom(message):
    try: 
        msg = eval(message.text.strip())
    except Exception as e:
        msg = "Sorry ! I can't understand,  Somthing Went worng .... "
    bot.reply_to (message,msg)


bot.polling()



import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler, CallbackQueryHandler

# Your bot token from the BotFather
TOKEN = '6450646063:AAHXX_Rf3Zqh-bqVNANNeMDzOzEHJrH7hTU'

# Create an Updater instance to receive updates from Telegram
updater = Updater(token=TOKEN, use_context=True)

# Get the dispatcher to register handlers
dp = updater.dispatcher

# Define a function to handle the /start command
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hello! I'm your bot. Send me a message, and I'll echo it back!")

# Define a function to echo back messages
def echo(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)

# Create command and message handlers
start_handler = CommandHandler('start', start)
echo_handler = MessageHandler(Filters.text & ~Filters.command, echo)

# Register the handlers
dp.add_handler(start_handler)
dp.add_handler(echo_handler)

# Start the bot
updater.start_polling()

# Run the bot until you send a signal to stop it
updater.idle()


import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Your bot token from the BotFather
TOKEN = '6450646063:AAHXX_Rf3Zqh-bqVNANNeMDzOzEHJrH7hTU'

# Create an Updater instance to receive updates from Telegram
updater = Updater(token=TOKEN, use_context=True)

# Get the dispatcher to register handlers
dp = updater.dispatcher

# Define a function to handle the /start command
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hello! I'm your bot. Send me a message, and I'll echo it back!")

# Define functions to handle custom commands
def hello(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hello!")

def hi(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hi there!")

def how_are_you(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="I'm just a bot, but thanks for asking!")

# Define a function to echo back messages
def echo(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)

# Create command and message handlers
start_handler = CommandHandler('start', start)
hello_handler = CommandHandler('hello', hello)
hi_handler = CommandHandler('hi', hi)
howareyou_handler = CommandHandler('howareyou', how_are_you)
echo_handler = MessageHandler(Filters.text & ~Filters.command, echo)

# Register the handlers
dp.add_handler(start_handler)
dp.add_handler(hello_handler)
dp.add_handler(hi_handler)
dp.add_handler(howareyou_handler)
dp.add_handler(echo_handler)

# Start the bot
updater.start_polling()

# Run the bot until you send a signal to stop it
updater.idle()



import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler, CallbackQueryHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

# Your bot token from the BotFather
TOKEN = '6450646063:AAHXX_Rf3Zqh-bqVNANNeMDzOzEHJrH7hTU'

# Create an Updater instance to receive updates from Telegram
updater = Updater(token=TOKEN, use_context=True)

# Get the dispatcher to register handlers
dp = updater.dispatcher

# Define states for conversation handling
START, ASK, LINK = range(3)

# Initialize user data dictionary
user_data = {}

# Define a function to start the conversation
def start(update, context):
    update.message.reply_text("Welcome! You can use the /ask command to ask a question.")
    return ASK

# Define a function to ask a question
def ask(update, context):
    user = update.message.from_user
    text = update.message.text
    user_data['question'] = text
    reply_text = f"Thanks for asking: {text}. Now, please provide a link to access in the following format: /link YourLinkHere"
    update.message.reply_text(reply_text)
    return LINK

# Define a function to provide a link
def link(update, context):
    user = update.message.from_user
    text = update.message.text
    user_data['link'] = text
    reply_text = f"Great! You asked: {user_data['question']}\n\nHere is the link you provided: {user_data['link']}"
    update.message.reply_text(reply_text)

    # You can also provide the link as a button
    keyboard = [[InlineKeyboardButton("Access Link", url=user_data['link'])]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text("Click the button below to access the link:", reply_markup=reply_markup)

    return ConversationHandler.END

# Define a function to cancel the conversation
def cancel(update, context):
    update.message.reply_text("The conversation has been canceled.")
    return ConversationHandler.END

# Create conversation handler
conv_handler = ConversationHandler(
    entry_points=[CommandHandler('ask', start)],
    states={
        ASK: [MessageHandler(Filters.text & ~Filters.command, ask)],
        LINK: [MessageHandler(Filters.text & ~Filters.command, link)]
    },
    fallbacks=[CommandHandler('cancel', cancel)]
)

# Register the conversation handler
dp.add_handler(conv_handler)

# Start the bot
updater.start_polling()

# Run the bot until you send a signal to stop it
updater.idle()

############################################

from typing import Final
from telegram import updater
from telegram.ext import Application ,CommandHandler,MessageHandler,filters,ContextTypes

# Commands 
TOKEN: Final  ="6450646063:AAHXX_Rf3Zqh-bqVNANNeMDzOzEHJrH7hTU"
BOT_USERNAME: FINAL = '@NtcGzbbot'

async def start_command(update: Update ,context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello ! Thanks  for chatting with me! I am a Ntc bot!")

async def Help_command(update: Update ,context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(" I am Ntc bot  !  Please type something o I Can Respond!s")

async def Custom_command(update: Update ,context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("This is Custom Command")

# Responses

def handle_reponse(text: str)->str:

    processed: str = text.lower() 


    if "hello "in Processed :
        return "hey there!"
    
    if "how are you "in Processed:
        return " I am good !"
    if "I love Python "in Processed:
        return "Remember to Subscribe it!" 


    return " I do not understand what you are wrote.....?"



async def handle_message (update: Update ,context: ContextTypes.DEFAULT_TYPE):
    message_type:str = update.message.chat.type
    text: str = update.message.text

    print (f'user ({update.message.chat,id })) in {messsage_type }: "{text}"')


    if message_type =='group':
        if BOT_USERNAME in text:
            new_text:str -text.replace(BOT_USERNAME,'').strip()
            response: str =handle_response(new_text)
        else:
            return
    else:
        response: str = handle_response(text)

    print('Bot',response)
    await update.message.reply_text(response)


async def error(update: Update,context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update } caused error {context.error}')



if __name__=='__main__':
    print('Starting Bot........')
    app = Aplicattion.builder().token(TOKEN).build()

    app.add_handler(CommandHandler('start',start_command))
    app.add_handler(CommandHandler('help',help_command))
    app.add_handler(CommandHandler('Custom',Custom_command))

# MEssages 
app.add_handler(MessageHandler(filters.TEXT,handle_message))


#error
app.add_error_handler(error)

#polling the bot

print('Polling')

app.run_polling(poll_interval=3)'''