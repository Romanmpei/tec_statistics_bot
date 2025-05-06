from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()

class Statistic(Base):
    __tablename__ = "statistics"

    id = Column(Integer, primary_key=True)
    category = Column(String)
    year = Column(String)
    text = Column(String)

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, unique=True, nullable=False)

# SQLite база в файле
engine = create_engine("sqlite:///src/statistics.db")
SessionLocal = sessionmaker(bind=engine)

def init_db():
    Base.metadata.create_all(bind=engine)
