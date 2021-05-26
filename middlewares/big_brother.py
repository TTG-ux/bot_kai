from aiogram import types

from aiogram.dispatcher.middlewares import BaseMiddleware
from aiogram.dispatcher.handler import CancelHandler

from data.config import banned_users


class BigBrother(BaseMiddleware):
    # 1
    async def on_pre_process_update(self, update: types.Update, data: dict):
        logging.info("[--------------------------Начало-------------------------------]")
        logging.info("1. Pre Process Update")
        logging.info("Следующая точка: Process Update")
        data["middleware_data"] = "Это пройдёт до on_process_update"
        if update.message:
            user = update.message.from_user.id
        elif update.callback_query:
            user = update.callback_query.from_user.id
        else:
            return

        if user not in banned_users:
            raise CancelHandler()

    # 2
    async def on_process_update(self, update: types.Update, data: dict):
        loggin.info(f"2. Process Update, {data}=")
        loggin.info("Следующая точка: Pre Process Message")

    # 3
    async def on_pre_process_message(self, message: types.Message, data: dict):
        loggin.info(f"3. Pre Process Message, {data}=")
        logging.info("Следующая точка: Filters")
        data["middleware_data"] = "Это пройдёт в on_process_message"

    # 4 Filters

    # 5
    async def on_process_message(self, message: types.Message, data: dict):
        loggin.info(f"4. Process Message")
        loggin.info("Следующая точка: Handler")
        data["middleware_data"] = "Это попадет в хендлер"

    # 6 Handler

    # 7