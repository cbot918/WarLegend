import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DB_URL")

# 建立引擎
engine = create_engine(DATABASE_URL, echo=True)  # echo=True 會印 SQL 出來 (debug 用)

# SessionLocal 會給 FastAPI 的 endpoint 使用
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base 給 ORM 繼承
Base = declarative_base()