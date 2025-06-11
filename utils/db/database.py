from sqlalchemy import create_engine, Column, String, Integer, BigInteger
from sqlalchemy.orm import declarative_base, session
from sqlalchemy.testing.suite.test_reflection import users

from quiz_bot.data.config import PG_USER, PG_HOST, PG_PASS, PG_PORT, PG_DB

engine = create_engine(f'postgresql+psycopg2://{PG_USER}:{PG_PASS}@{PG_HOST}:{PG_PORT}/{PG_DB}')


Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    chat_id = Column(BigInteger,unique=True)
    name = Column(String(50),nullable=False, unique=True)
    phone = Column(String(12),nullable=False, unique=True)


if __name__ == '__main__':
    # User obyektini yaratish va qo‘shish (xohlasang)
    # user = User(chat_id=5937680085, fullname='Jaloliddin Jumanov')
    # session.add(user)

    # User ni chat_id orqali izlash
    user = session.query(User).filter(User.chat_id == 5937680085).first()

    if user:
        user.fullname = 'Jumanov Jaloliddin'
        print(f"Foydalanuvchi yangilandi: {user.fullname}")
    else:
        print("Foydalanuvchi topilmadi.")

    session.commit()
