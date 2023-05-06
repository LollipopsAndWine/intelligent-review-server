from datetime import datetime
from sqlalchemy import Boolean, Column, Integer, String, TEXT, DateTime
from ..common.database import Base


class Rules(Base):
    __tablename__ = 'rules'  # 定义表名
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    rule_name = Column(String(128), unique=True)
    rule_config = Column(TEXT)
    is_delete = Column(Boolean, default=False)
    create_time = Column(DateTime, default=datetime.now)
    update_time = Column(DateTime, default=datetime.now, onupdate=datetime.now)
