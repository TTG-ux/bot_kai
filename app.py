from aiogram import executor

from loader import dp
import middlewares, filters, handlers
from utils.notify_admins import on_startup_notify




async def on_startup(dispatcher):
    middlewares.setup(dispatcher)
    handlers.users.setup(dispatcher)

    await on_startup_notify(dispatcher)



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True,  on_startup=on_startup)
