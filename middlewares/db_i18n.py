
from typing import Dict, Any

from aiogram.types import TelegramObject
from aiogram.utils.i18n import I18nMiddleware

from utils.db.database import session
from utils.db_helper import get_user_db_lang


class DatabaseI18nMiddleware(I18nMiddleware):
    async def get_locale(self, event: TelegramObject, data: Dict[str, Any]) -> str:
        user = data.get('event_from_user')
        user_lang = await get_user_db_lang(session, user.id)
        return user_lang or self.i18n.default_locale
