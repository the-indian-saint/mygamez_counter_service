from typing import Optional

from pydantic import BaseModel

#from .database import Base

#from sqlalchemy import Integer, String

#from sqlalchemy.orm import relationship

class Counter(BaseModel):
    name: Optional[str] = None
    count: Optional[int] = 0

    #class Config:
        #orm_mode = True


class CounterCreate(BaseModel):
    name: str

    #class Config:
        #orm_mode = True



#class counter(Base):
#    __tablename__ = "Counters"

#    name = Column(String)
#    count = Column(Integer)
