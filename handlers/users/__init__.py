from .start import dp
from .start import bot_start
import logging
from .purchase import dp


from aiogram import Dispatcher, filters


def setup(dp: Dispatcher):
    dp.register_message_handler(bot_start, filters.CommandStart())
    logging.info("Handlers are successfully configured")
