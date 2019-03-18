import json
import re
from lib import fetchRSSFeed, sendNotification

subreddits = ''
for line in open('subreddits.json', 'r'):
  subreddits += line
  
subreddits = json.loads(subreddits)['subreddits']

def checkReddit():
  for sr in subreddits:
    feed = fetchRSSFeed(sr["name"])
    for post in feed.entries:
      match = re.search(r'|'.join(sr["keywords"]), post.title, re.I)
      if match:
        print('sending notification')
        sendNotification(post, sr["name"])

# checkReddit()

def handler(event, context):
  sendNotification({ "link":"The service is working" }, 'TEST')
  checkReddit()
