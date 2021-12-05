from bot import start_bot
from dotenv import (
    find_dotenv,
    load_dotenv
)
from os import environ

if __name__ == "__main__":
    load_dotenv(find_dotenv())

    token = environ.get("TELEGRAM_TOKEN")
    start_bot(token)