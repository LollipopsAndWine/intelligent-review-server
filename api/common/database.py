from .extensions import configMap, parse_uri
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

config = configMap()
# 创建数据库引擎
SQLALCHEMY_DATABASE_URI = parse_uri(config.DATABASE_URI)
engine = create_engine(SQLALCHEMY_DATABASE_URI)
# 创建数据库会话
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# 声明基类
Base = declarative_base()


def get_db():
    Base.metadata.create_all(engine)
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
