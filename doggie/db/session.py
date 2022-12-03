from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine(config.SQLALCHEMY_DATABASE_URI, connect_args={'check_same_thread': False})

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
