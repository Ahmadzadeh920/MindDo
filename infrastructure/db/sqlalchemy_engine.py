from sqlalchemy.orm import declarative_base, sessionmaker
from  sqlalchemy import create_engine
from infrastructure.config.settings import settings


Base = declarative_base()

engine = create_engine(settings.DATABASE_URL ,echo=False )