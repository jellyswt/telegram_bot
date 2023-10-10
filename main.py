from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import (
    CallbackContext,
    Updater,
    PicklePersistence,
    CommandHandler,
    MessageHandler,
    Filters,
    CallbackQueryHandler
)
from cred import TOKEN
from menu import (
    main_menu_keyboard,
    courses_menu_keyboard
)
from key_buttons import tele_buttons, courses

ABOUT = tele_buttons[0]
COURSES = tele_buttons[1]
BACK = courses[4]
PYTHON = courses[0]
JAVA = courses[1]
JS = courses[2]
QA = courses[3]
LOCATION = tele_buttons[2]


def start(update:Update, context:CallbackContext):
    update.message.reply_text(
        f'welcome {update.effective_user.username},\n this bot will help you with info about gyuvins dog',
        reply_markup=main_menu_keyboard()
    )
def main_menu(update:Update, context:CallbackContext):
    update.message.reply_text(
        f'main menu',
        reply_markup=main_menu_keyboard()
    )
def about(update:Update, context:CallbackContext):
    update.message.reply_text(
        f'gyuvin has an ugly dog called eumppappa. he likes to dress him up and take him on long walks',
    )
def reply_courses(update:Update, context:CallbackContext):
    update.message.reply_text(
        f'choose course',
        reply_markup=courses_menu_keyboard()
    )
def python(update:Update, context:CallbackContext):
    update.message.reply_text(
        f'ill put text later srry too lazy rn',
    )
def java(update:Update, context:CallbackContext):
    update.message.reply_text(
        f'same here too lazy TT',
    )
def js(update:Update, context:CallbackContext):
    update.message.reply_text(
        f'hyd i hope everything is alr',
    )
def qa(update:Update, context:CallbackContext):
    update.message.reply_text(
        f'eumppappa is so cute acc its not ugly',
    )

def location(update:Update, context:CallbackContext):
    msg = context.bot.send_message(
        update.effective_chat.id,
        text = 'location of eumppappa'
    )
    update.message.reply_location(
        #42.82909025000069,74.61687279022618
        longitude=74.61687279022618,
        latitude=2.82909025000069,
        reply_to_message_id=msg.message_id
    )

updater = Updater(token=TOKEN, persistence=PicklePersistence(filename='bot_data'))
updater.dispatcher.add_handler(CommandHandler('start', start))

updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(ABOUT),
    about
))
updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(COURSES),
    reply_courses
))
updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(BACK),
    main_menu
))
updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(PYTHON),
    python
))
updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(JAVA),
    java
))
updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(JS),
    js
))
updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(QA),
    qa
))
updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(LOCATION),
    location
))




updater.start_polling()
updater.idle()