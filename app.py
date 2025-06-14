
import asyncio
import logging
import sys
from os import getenv

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.utils.i18n import I18n

from dotenv import load_dotenv

from middlewares.db_i18n import DatabaseI18nMiddleware
from utils.notify_admins import bot_start_up, bot_shut_down
from handlers import *

load_dotenv()
TOKEN = getenv("BOT_TOKEN")
dp = Dispatcher()


async def main() -> None:
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    dp.include_routers(start_router, register_router, menu_router)


    dp.startup.register(bot_start_up)
    dp.shutdown.register(bot_shut_down)

    i18n = I18n(path="locales", default_locale="uz", domain="messages")
    dp.update.outer_middleware.register(DatabaseI18nMiddleware(i18n))

    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
