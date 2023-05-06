from datetime import datetime
from sqlalchemy import Boolean, Column, Integer, String, TEXT, DateTime
from ..common.database import Base


class AdipTask(Base):
    __tablename__ = 'adip_task'  # 定义表名
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    project_id = Column(Integer)
    project_name = Column(String(128))
    data_key = Column(String(128))
    data = Column(TEXT)
    is_delete = Column(Boolean, default=False)
    create_time = Column(DateTime, default=datetime.now)
    update_time = Column(DateTime, default=datetime.now, onupdate=datetime.now)
