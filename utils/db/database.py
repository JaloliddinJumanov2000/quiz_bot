from sqlalchemy import create_engine, Column, String, Integer, BigInteger
from sqlalchemy.orm import declarative_base
from quiz_bot.data.config import PG_USER, PG_HOST, PG_PASS, PG_PORT, PG_DB

engine = create_engine(f'postgresql+psycopg2://{PG_USER}:{PG_PASS}@{PG_HOST}:{PG_PORT}/{PG_DB}')


Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    chat_id = Column(BigInteger,unique=True)
    name = Column(String(50),nullable=False, unique=True)
    phone = Column(String(12),nullable=False, unique=True)
