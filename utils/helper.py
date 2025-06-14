from keyboards.reply.button import menu
from utils.db.database import User, session
from aiogram.utils.i18n import gettext as _


def check_register(func):
    async def wrapper(*args, **kwargs):
        message = args[0]
        chat_id = message.chat.id
        if User.check_register(session, chat_id):
            await message.answer(_('Botdan foydalanishga xush kelibsiz!'), reply_markup=menu())
        else:
            if func.__name__ == 'register_start':
                await func(message, kwargs.pop('state'))
            else:
                await func(message)

    return wrapper