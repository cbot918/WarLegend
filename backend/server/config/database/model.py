from sqlalchemy import Column, String, Integer, TIMESTAMP
from sqlalchemy.sql.sqltypes import Numeric

from db import Base

class DayDataTemp(Base):
    __tablename__ = "daydata_temp"
    # __table_args__ = {"extend_existing": True}
    date = Column(String(8), primary_key=True)   # YYYYMMDD
    spy_upper = Column(Integer, nullable=False)
    spy_lower = Column(Integer, nullable=False)
    qqq_upper = Column(Integer, nullable=False)
    qqq_lower = Column(Integer, nullable=False)
    swing_spy_upper = Column(Integer, nullable=True)
    swing_spy_lower = Column(Integer, nullable=True)
    swing_qqq_upper = Column(Integer, nullable=True)
    swing_qqq_lower = Column(Integer, nullable=True)
    updated_at = Column(TIMESTAMP(timezone=True), nullable=False)
    deleted_at = Column(TIMESTAMP(timezone=True), nullable=True)
    created_by = Column(String(100), nullable=False)

class DayData(Base):
    __tablename__ = "daydata"

    date = Column(String(8), primary_key=True)              # YYYYMMDD
    trade_type = Column(String(16), primary_key=True)       # 複合主鍵之一
    item = Column(String(10), primary_key=True)             # 複合主鍵之一
    upper = Column(Numeric(10, 2), nullable=False)          # NUMERIC(10,2)
    lower = Column(Numeric(10, 2), nullable=False)          # NUMERIC(10,2)
    updated_at = Column(TIMESTAMP(timezone=True), nullable=False)  # 含時區
    created_by = Column(String(100), nullable=False)