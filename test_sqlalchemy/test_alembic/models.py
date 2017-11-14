from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class TestTable(Base):
    __tablename__ = 'TestTable'
    Id = Column(Integer, primary_key=True)
    TestColumn = Column(String)
    AddedColumn = Column(String)
    Created = Column(DateTime, default=func.now())


class AnotherTestTable(Base):
    __tablename__ = "AnotherTestTable"
    Id = Column(Integer, primary_key=True)
    Letters = Column(String)
    Numbers = Column(Float)

class TableThree(Base):
    __tablename__ = "TableThree"
    Id = Column(Integer, primary_key=True)
    AnotherTestTableId = (Integer)
