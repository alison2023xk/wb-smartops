from sqlalchemy import Column,Integer,Float,String,Date,JSON
from sqlalchemy.ext.declarative import declarative_base
from database.db import engine
Base=declarative_base()
class SalesFunnel(Base):
    __tablename__='sales_funnel'
    id=Column(Integer,primary_key=True)
    nmId=Column(Integer)
    date=Column(Date)
    openCount=Column(Integer)
    cartCount=Column(Integer)
    orderCount=Column(Integer)
    buyoutCount=Column(Integer)
Base.metadata.create_all(engine)