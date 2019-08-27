import praw
import time
import datetime
from enum import IntEnum

#config
start_time = datetime.datetime(2019, 8, 26, 14, 45, 0, 0)
post_delay = datetime.timedelta(hours=1)

class LinkData(IntEnum):
    Subreddit = 0
    URL = 1
    Title = 2

f = open('links.txt')
lines = list(f)
links = []
for l in lines:
    if not l.startswith('#'):
        links.append(l.split(','))
        print(l)


print('Start at: ', start_time)
print('Delay: ', post_delay.total_seconds())
print('Links: ', len(links))

reddit = praw.Reddit('bot')

keepGoing = True
while(keepGoing):
    if datetime.datetime.now() > start_time:
        for current in links:
            subreddit = reddit.subreddit(current[LinkData.Subreddit])
            subreddit.submit(current[LinkData.Title], url=current[LinkData.URL])
            print(datetime.datetime.now())
            time.sleep(post_delay.total_seconds())
        keepGoing = False
    time.sleep(60)

print("end")
