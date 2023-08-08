from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Initialize SQLite database
DATABASE_URL = "sqlite:///data_employee.db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


class Employee(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True, index=True)
    empno = Column(String, unique=True, index=True)
    ename = Column(String)
    job = Column(String)
    deptno = Column(String)


class Department(Base):
    __tablename__ = "departments"

    id = Column(Integer, primary_key=True, index=True)
    deptno = Column(String, unique=True, index=True)
    dname = Column(String)
    loc = Column(String)


Base.metadata.create_all(bind=engine)
