# RSS Feed Reader

By definition an RSS reader is a tool that allows a user to receive updates from a blog or podcast. RSS have become scarse and possiblly a medeaval approach to how users receive updates from their favorite websites.

This project is created in an attempt to create a database of feeds a user would like to keep up with base on unique topics (eg. sports, politics, or titles suchs as podcast and music)

## System Requirements

### Features

- [x] Reader
  
  Reader creates a simple command line application that gets inputs from the user. Accepts RSS URL, loads the downloaded xml and deserializes the response into objects which are persisted into a database.

- [ ] Cron Job
  
  Creates a cron job for each topic and RSS feeds to check for new post or feed. Publish messages to Apache Kafka to notify consumers of updates or new Feeds.

- [ ] RSS Reader Application
  
  This application consumes the messages, receives feeds from the cron jobs by registering kafka topics. This application receives these feeds in real time.
