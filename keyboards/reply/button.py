from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from aiogram.utils.i18n import gettext as _


def confirm_button():
    keyboards = [

        [
            KeyboardButton(text=_('Ha')),
            KeyboardButton(text=_('Yo`q'))
        ],

    ]
    kb = ReplyKeyboardMarkup(keyboard=keyboards,
                             resize_keyboard=True,
                             input_field_placeholder=_('Tugamadan foydalaning!'))
    return kb


def share_contact():
    keyboards = [
        [
            KeyboardButton(text=_('📲 Telefon ulashish'), request_contact=True),
        ]

    ]
    kb = ReplyKeyboardMarkup(keyboard=keyboards,
                             resize_keyboard=True,
                             input_field_placeholder=_('Tugamadan foydalaning!'))
    return kb


def menu():
    keyboards = [
        [
            KeyboardButton(text=_("Testlar")),
            KeyboardButton(text=_("Natijalar")),

        ]
    ]
    kb = ReplyKeyboardMarkup(keyboard=keyboards, resize_keyboard=True)
    return kb