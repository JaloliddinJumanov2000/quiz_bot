from aiogram import Router, html
from aiogram.filters import CommandStart
from aiogram.types import Message

from utils.db.database import User, session
from utils.helper import check_register
from aiogram.utils.i18n import gettext as _

start_router = Router()


@start_router.message(CommandStart())
@check_register
async def command_start_handler(message: Message):
    fullname = html.bold(message.from_user.full_name)
    await message.answer(
        _("Salom, {name}!\n\n Ro'yxatdan o'tish uchun  👉 /register kamandasini bosing").format(name=fullname))