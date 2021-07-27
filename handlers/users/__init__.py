from .start import dp
from .start import bot_start
import logging
from . import purchase
from . import mat_ikt_menu
from . import mat_khem_menu
from . import Bachelor_course_main
from . import iktfiz_degree_manu
from . import Master_degree_program
from . import Distans_ikt_main
from . import Distance_learning
from . import maga_main
from . import Distans_maga
from . import maga_degree
from . import middle_school
from . import theend

from aiogram import Dispatcher, filters


def setup(dp: Dispatcher):
    dp.register_message_handler(bot_start, filters.CommandStart())
    logging.info("Handlers are successfully configured")
