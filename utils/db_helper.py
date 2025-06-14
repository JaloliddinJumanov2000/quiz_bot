from utils.db.database import User


async def get_user_db_lang(session, chat_id):
    user = session.query(User).filter(chat_id == User.chat_id).first()
    return user.lang if user else None