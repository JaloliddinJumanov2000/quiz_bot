
from aiogram import Router, F
from aiogram.types import Message
from aiogram.utils.i18n import gettext as _
from aiogram.utils.i18n import lazy_gettext as __

menu_router = Router()


@menu_router.message(F.text == __('Testlar'))
async def test_handler(message: Message):
    await message.answer(_("Barcha testlar"))


@menu_router.message(F.text == __('Natijalar'))
async def test_handler(message: Message):
    await message.answer(_("Barcha Natijalar"))
