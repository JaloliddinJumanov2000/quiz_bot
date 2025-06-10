from sqlalchemy import create_engine
from data.config import PG_USER

engine = create_engine('postgresql+psycopg2://database.db', echo=True)