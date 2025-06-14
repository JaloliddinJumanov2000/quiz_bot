from aiogram import Router, F
from aiogram.types import CallbackQuery
from aiogram.utils.i18n import I18nContext

router = Router()

@router.callback_query(F.data.startswith("lang_"))
async def change_language(callback: CallbackQuery, i18n: I18nContext):
    lang = callback.data.split("_")[1]
    await i18n.set_locale(lang)
    await callback.message.answer(
        i18n.gettext("Til muvaffaqiyatli o'zgartirildi!")  # bu yozuv messages.po faylda bo‘lishi kerak
    )
