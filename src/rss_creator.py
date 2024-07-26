from program_menu import MainMenu
from bs4 import BeautifulSoup
from src.models import Feed
from sqlalchemy.orm import Session
from logging import Logger
import requests
import time
import logging
import re

# Create a global log variable to facilitate logging for the whole module
log = logging.getLogger(__name__)

class RssCreator:
  """
  This class creates rss feeds from data fed into it
  """

  def __init__(self) -> None:
    logging.basicConfig(level=logging.INFO)
    
  def get_logging(self):
    return log

  def scan(self, url, retry = False):
    log.info(f"Scanning {self.name}...")
    try:
      resp = requests.get(url)
      soup = BeautifulSoup(resp.content, "xml")
      # output_file = Path("./var/" + name + ".xml")
      # output_file.parent.mkdir(exist_ok=True, parents=True)
      # output_file.write_text(soup.text)

      self.entries = soup.find_all("item")
      log.info(f"Completed scanning. Total entries: {len(self.entries)}")
    except Exception as e:
      log.error("Error connecting to host", e)
      
      if not retry:
        log.info("Retrying...")
        time.sleep(5000)
        self.scan(url, True)
      else:
        log.error("Failed the second try!")

  def get_feeds(self, count):
    not_none = lambda v : v.string if v != None else ''
    
    feeds = []
    for entry in self.entries[:count]:
      feed = Feed()
      if not_none(entry.title).split(":")[0].strip() == "Lateral":
        feed.id = 0
      else:
        feed.id = int(not_none(entry.title).split(":")[0].strip())
      feed.title = not_none(entry.title).split(":")[1].strip()
      feed.summary = not_none(entry.summary)
      feed.link = not_none(entry.link)
      
      feeds.append(feed)
    return feeds
      
  def save_latest_feed(self, n = 1):
    log.info(f"Saving latest feeds...")
    feeds = self.get_feeds(n)
    session = Session(self.engine)
    session.add_all(feeds)
    session.commit()
    session.close()
    
    log.info(f"Completed saving feeds. Total saved: {n}")
  
  def print_feed(self, feed):
    divider = "".join(['#' for i in range(30)])
    log.info(f"\n{divider}\n# Feed: {feed.id}: {feed.title}\n#\n# Link:{feed.link}\n{divider}\n")
  
  def get_latest_feed(self, n):
    
    log.info(f"Retrieving latest feeds...")
    with Session(self.engine) as session:
      feeds: list[Feed] = session.query(Feed).order_by(Feed.id.asc()).all()

      log.info(f"Logging requested feed: Number: {n}")
      filter_list = lambda c, feed_list : feed_list[:c] if c != None else feed_list[:len(feed_list)] 
      filtered_list = filter_list(n, feeds)
      for feed in filtered_list:
        self.print_feed(feed)
        
  def get_feed_by_id(self, id):
    if id != None:
      with Session(self.engine) as session:
        feed = session.query(Feed).filter(Feed.id == id).first()
        self.print_feed(feed) if feed != None else log.info(f"Feed with id: {feed.id} not found!")
      
  def start(self, engine):
    """Steps:
    - show a menu (options: url/uri, get latest feed, get top n latest feeds, get all feeds)
    - for each implement and update database
    - uri/url - create a topic and save to the database
      - fields; title, summary and 
    - create a background cron job for each topic to update feeds database
    """
    self.engine = engine
    options = {
      0: "Exit",
      1: "Enter URI/URL to scan",
      2: "Save latest feed",
      3: "Save top n feeds",
      4: "Save all feeds",
      5: "Get latest feed",
      6: "Get top n feeds",
      7: "Get all feeds",
      8: "Get Feed by id"
    }
    menu = MainMenu(options=options)
    
    while (menu.get_selected_option() != 0):
      menu.show_options()
      menu.set_selected_option(int(input('\n>> ')))

      if menu.get_selected_option() == 1:
        url = input("Enter Url/Uri >> ")
        self.name = input("Enter a unique name >> ")
        self.scan(url)
      elif menu.get_selected_option() == 2:
        self.save_latest_feed()
      elif menu.get_selected_option() == 3:
        n = int(input("Enter number >> "))
        self.save_latest_feed(n)
      elif menu.get_selected_option() == 4:
        self.save_latest_feed(len(self.entries))
      elif menu.get_selected_option() == 5:
        self.get_latest_feed(1)
      elif menu.get_selected_option() == 6:
        n = int(input("Enter number >> "))
        self.get_latest_feed(n)
      elif menu.get_selected_option() == 7:
        self.get_latest_feed()
      elif menu.get_selected_option() == 8:
        id = int(input("Enter number >> "))
        self.get_feed_by_id(id)