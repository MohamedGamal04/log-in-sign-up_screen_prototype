import pandas as pd
from sqlalchemy import *
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base
def Main(first_name ,last_name,username,gender,email,password,country,address,age):
    engine=create_engine("mysql://root:123@localhost/myDB")

    Session=sessionmaker(bind=engine)
    session=Session()
    Base=declarative_base()

    class Account(Base):
        __tablename__="accounts"
        ssn=Column(Integer,primary_key=True,autoincrement=True)
        first_name=Column(String(20))
        last_name=Column(String(20))
        username=Column(String(20))
        gender=Column(CHAR(1))
        email=Column(String(30))
        password=Column(String(20))
        country=Column(String(20))
        address=Column(String(50))
        age=Column(Integer)
        def __init__(self,fname,lname,username,gender,email,password,country,address,age):
            self.first_name=fname
            self.last_name=lname
            self.username=username
            self.gender=gender
            self.email=email
            self.password=password
            self.country=country
            self.address=address
            self.age=age
            session.add(self)
            session.commit()
        def __repr__(self):
            return f"{self.first_name} {self.last_name},{self.email},{self.password},{self.age}"
    Base.metadata.create_all(engine)
    Account(first_name ,last_name,username,gender,email,password,country,address,age)
