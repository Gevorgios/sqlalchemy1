from sqlalchemy import create_engine, Column, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Recipe(Base):
    __tablename__ = 'recipes'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    author = Column(String)
    recipe_type = Column(String)
    description = Column(Text)
    video_link = Column(String)
    ingredients = Column(Text)
    cuisine = Column(String)