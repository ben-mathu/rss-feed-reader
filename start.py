from src.rss_creator import RssCreator
from sqlalchemy import create_engine
from src.models import BaseModel
import logging

if __name__ == '__main__':
  rss_creator = RssCreator()
  rss_creator.get_logging().info("Initialiazing...")
  
  engine = create_engine("sqlite://", echo=True)
  BaseModel.metadata.create_all(engine)
  
  rss_creator.start(engine)