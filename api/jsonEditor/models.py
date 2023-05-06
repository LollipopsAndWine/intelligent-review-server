from datetime import datetime
from sqlalchemy import Boolean, Column, Integer, String, TEXT, DateTime
from ..common.database import Base


# 定义 User 类
class JsonSchema(Base):
    __tablename__ = 'json_schema'  # 定义表名
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    schema_name = Column(String(128), unique=True)
    json_schema = Column(TEXT)
    is_delete = Column(Boolean, default=False)
    create_time = Column(DateTime, default=datetime.now)
    update_time = Column(DateTime, default=datetime.now, onupdate=datetime.now)
