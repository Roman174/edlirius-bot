from telegram import Update
from telegram.ext import (
    Updater,
    MessageHandler,
    Filters,
    CallbackContext,
)

from info import load_info


def on_receive_serial_number(update: Update, context: CallbackContext) -> None:
    serial = update.message.text
    if not validate_serial(serial):
        update.message.reply_text("Неверный формат данных!")
    else:
        info = load_info(serial)
        update.message.reply_text(info)


def validate_serial(serial: str) -> bool:
    elements = serial.split("\n")
    elements_len = len(elements)

    return elements_len != 0 and elements_len <= 10


def start_bot(token: str):
    updater = Updater(token)
    updater.dispatcher.add_handler(MessageHandler(Filters.text, on_receive_serial_number))

    updater.start_polling()
    updater.idle()