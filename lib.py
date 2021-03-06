import feedparser
import smtplib
from email.message import EmailMessage
import os

from dotenv import load_dotenv
load_dotenv(verbose=True, dotenv_path="variables.env")

latestPostIds = {}

def fetchRSSFeed(subreddit):
  query = "?limit=100"
  if subreddit in latestPostIds:
    query += f"&before + {latestPostIds[subreddit]}"
  feed = feedparser.parse(f"https://www.reddit.com/r/{subreddit}/new.rss{query}")

  if (len(feed.entries) > 0):
    latestPostIds[subreddit] = feed.entries[0].id.split("/")[-1]
  return feed

def sendNotification(posts, sr):
  port = os.getenv("MAIL_PORT")
  host = os.getenv("MAIL_HOST")
  sender = os.getenv("MAIL_SENDER")
  password = os.getenv("MAIL_PW")
  receiver = os.getenv("MAIL_RECEIVER")

  msg = EmailMessage()
  msg["From"] = sender
  msg["To"] = receiver
  msg["Subject"] = "New interesting post on subreddit " + sr

  body = "\n\n".join(list(map(lambda post : f"{post['title']}\n{post['link']}", posts)))
  msg.set_content(body)

  server = smtplib.SMTP(host, port)
  server.ehlo()
  server.starttls()
  server.login(sender, password)
  server.send_message(msg)
  print("Sent notification to " + receiver)