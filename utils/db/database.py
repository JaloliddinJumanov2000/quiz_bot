from sqlalchemy import (create_engine, Column, Integer,
                        String, BigInteger)
from sqlalchemy.orm import declarative_base, sessionmaker
from data.config import PG_USER, PG_PASS, PG_HOST, PG_PORT, PG_DB

engine = create_engine(f'postgresql+psycopg2://{PG_USER}:{PG_PASS}@{PG_HOST}:{PG_PORT}/{PG_DB}')

Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    chat_id = Column(BigInteger, unique=True)
    fullname = Column(String(50), nullable=False)
    phone = Column(String(12))


if __name__ == '__main__':
    user = User(chat_id=1836679375, fullname='Asadbek Solijonov', phone='998911779116')
    session.add(user)
    # user = session.query(User).filter(1836679375 == User.chat_id).first()
    # if user:
        # user.fullname = 'Solijonov Asadbek'
        # session.delete(user)
    session.commit()