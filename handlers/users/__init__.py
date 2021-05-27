from .start import dp
from .purchase import dp
import logging

from .start import bot_start

from aiogram import Dispatcher, filters


def setup(dp: Dispatcher):
    dp.register_message_handler(bot_start, filters.CommandStart())
    logging.info("Handlers are successfully configured")
