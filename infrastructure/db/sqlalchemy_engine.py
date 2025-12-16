from sqlalchemy.orm import declarative_base, sessionmaker
from  sqlalchemy import create_engine
from infrastructure.config.settings import settings


Base = declarative_base()

engine = create_engine(settings.DATABASE_URL ,echo=False )
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
def get_db_session():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()