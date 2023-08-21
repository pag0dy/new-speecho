from sqlalchemy import Column,Integer, String
from .database import Base

class Transcript(Base):
    __tablename__ = "transcript"
    id = Column(Integer, primary_key=True, index=True)
    user_email = Column(String)
    audiofile_name = Column(String)
    