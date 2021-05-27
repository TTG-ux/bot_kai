from aiogram import executor

from loader import dp
import middlewares, filters, handlers
from utils.notify_admins import on_startup_notify
from utils.dp_api.database import create_db




async def on_startup(dispatcher):
    middlewares.setup(dispatcher)
    handlers.users.setup(dispatcher)

    await on_startup_notify(dispatcher)
    await create_db()


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup, skip_updates=True)
