from aiogram import Dispatcher

from loader import dp

# from .throttling import ThrottlingMiddleware
from .throttling import ThrottlingMiddleware

if __name__ == '__main__':
    # dp.middleware.setup(ThrottlingMiddleware())
    dp.middleware.setup(ThrottlingMiddleware())
