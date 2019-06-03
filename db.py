from sqlalchemy import create_engine, Column
from sqlalchemy import Integer, BigInteger, String, Text, LargeBinary, DateTime, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Create a (lazy) database engine
engine = create_engine("sqlite:///database.sqlite")

# Create a base class to define all the database subclasses
TableDeclarativeBase = declarative_base(bind=engine)

# Create a Session class able to initialize database sessions
Session = sessionmaker()


class User(TableDeclarativeBase):
    # primary_key=True will set id automatically
    id = Column(Integer, primary_key=True)
    # Telegram data
    user_id = Column(BigInteger)
    first_name = Column(String)
    last_name = Column(String)
    username = Column(String)

    # Extra table parameters
    __tablename__ = 'users'

    def __repr__(self):
        return f'User {self.user_id}'


# This will create tables in db, run only one time for creating db
TableDeclarativeBase.metadata.create_all()








