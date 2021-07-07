from .start import dp
from .start import bot_start
import logging
from .purchase import dp
from . import Feedback
from . import mat_ikt_menu
from . import mat_khem_menu
from . import mat_sosity_menu
from . import Bachelor_course_main
from . import iktfiz_degree_manu
from . import Master_degree_program


from aiogram import Dispatcher, filters


def setup(dp: Dispatcher):
    dp.register_message_handler(bot_start, filters.CommandStart())
    logging.info("Handlers are successfully configured")
