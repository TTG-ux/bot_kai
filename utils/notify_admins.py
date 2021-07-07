from data.config import admin
from aiogram import Dispatcher
import logging



async def on_startup_notify(dp: Dispatcher):
    for admin_main in admin:
        try:
            await dp.bot.send_message(admin_main, "Бот Запущен")

        except Exception as err:
            logging.exception(err)


