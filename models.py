from database import Base
from sqlalchemy import Column, Integer, String, Boolean, Float

class Task(Base):
  __tablename__ = 'tasks'

  id = Column(Integer, primary_key=True, index=True)
  name = Column(String)
  category = Column(String)
  description = Column(String)
  isFinished = Column(Boolean)
  createdDate = Column(String)
  dueDate = Column(String)
  priority = Column(Integer)