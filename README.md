# RSS Feed Reader

RSS (Really Simple Syndication) feed reader is a simple Python tool that allows a user to aggregate feeds from a blog, website or podcast and saves this data in databases.
This helps to easily keep track of favorite sites while receiving customized updates of the news outlets or topics registered.

This project was built in an attempt to create a backend service and application to keep track of feeds a user would like to keep up with based on unique topics (eg. sports, politics, or titles suchs as those for podcast and music)

## Data flow

- User registers a feed by providing a URL of the feed.
- Each RSS feed registered has a topic that is registered as single schedule so a scheduler is created to track updates from the feed.
- Backend service that aggragates data from the feed and saves the data on a database for every scheduled interval.
- A message stream is registered to track new entries and sends a notification to the user via email, sms or push notification.
- REST APIs are used to retrieve data from the database, feeding the user details about the feed and its updates through an application.
- The user receives feeds/updates and opens the article or navigate to their favorite website or app to consume the feed.

## System Requirements

### Features

- [x] Reader
  
  Reader creates a simple command line application that gets inputs from the user. Accepts RSS URL, loads the downloaded xml and deserializes the response into objects which are persisted into a database.

- [ ] Scheduling Tool
  
  Creates a cron job for each topic and RSS feeds to check for new post or feed. Publish messages to Apache Kafka to notify consumers of updates or new Feeds.

- [ ] RSS Reader Application
  
  This application consumes the messages, receives feeds from the cron jobs by registering kafka topics. This application receives these feeds in real time.
