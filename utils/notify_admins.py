import logging

from aiogram import Bot, html

from data.config import ADMINS


async def bot_start_up(bot: Bot):
    try:
        for admin in ADMINS:
            await bot.send_message(chat_id=admin, text=html.italic("Bot ishga tushdi!"))
    except Exception as e:
        logging.info(f"{e}")


async def bot_shut_down(bot: Bot):
    try:
        for admin in ADMINS:
            await bot.send_message(chat_id=admin, text=html.italic("Bot o'chdi!"))
    except Exception as e:
        logging.info(f"{e}")