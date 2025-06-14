from aiogram import Router, F, html
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.fsm.context import FSMContext

from keyboards.reply.button import confirm_button, share_contact, menu
from states.register import RegisterState
from utils.db.database import User, session
from utils.helper import check_register
from aiogram.utils.i18n import gettext as _

register_router = Router()


@register_router.message(Command('register'))
@check_register
async def register_start(message: Message, state: FSMContext):
    await message.answer(_('To`liq ismingiz: '))
    # 1-qadam
    await state.set_state(RegisterState.fullname)


@register_router.message(RegisterState.fullname)
async def fullname_handler(message: Message, state: FSMContext):
    fullname = message.text
    # filter
    await state.update_data(fullname=fullname)
    await message.answer(_('Telefon raqamingizni kiriting!'), reply_markup=share_contact())
    await state.set_state(RegisterState.phone)


@register_router.message(RegisterState.phone)
async def phone_handler(message: Message, state: FSMContext):
    phone_number = message.text  # filter qiling

    if message.contact:
        phone_number = message.contact.phone_number

    await state.update_data(phone=phone_number)

    datas = await state.get_data()
    fullname = datas.get('fullname')
    phone = phone_number
    user_chat_id = message.from_user.id
    user_data = _("Ma`lumotlaringizni tasdiqlaysizmi?\n\n"
                  "To'liq ism: {fullname}\n"
                  "Telefon: {phone}\n"
                  "Chat ID: {user_id}\n").format(fullname=html.bold(fullname),
                                                 phone=html.bold(phone),
                                                 user_id=html.bold(user_chat_id))

    await message.answer(user_data, reply_markup=confirm_button())
    await state.set_state(RegisterState.confirm)


@register_router.message(RegisterState.confirm)
async def confirm_handler(message: Message, state: FSMContext):
    confirm = message.text

    if confirm.casefold() == _('ha'):
        datas = await state.get_data()
        fullname = datas.get('fullname')
        phone = datas.get('phone')
        user_chat_id = message.from_user.id

        # database saqlashga tayyorlash
        user = User(fullname=fullname, phone=phone, chat_id=user_chat_id)
        user.save(session)

        await message.answer(_('Botdan foydalanishga xush kelibsiz!'), reply_markup=menu())
        await state.clear()

    # Yoq: /register ga qaytaramiz!
    elif confirm.casefold() == _('yo`q'):
        await message.answer(_('Qayta ro`yxatdan o`tish uchun  👉 /register kamandasini bosing'),
                             reply_markup=ReplyKeyboardRemove())
        await state.clear()
    else:
        await message.reply(_('Ha yoki Yo`q bilan tasdiqlang iltimos!'))