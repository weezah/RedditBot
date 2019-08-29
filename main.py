import praw
import time
import datetime
import links
import msvcrt
from enum import IntEnum

#config
post_delay = datetime.timedelta(minutes=15)

links = links.Links()
reddit = praw.Reddit('bot')

print('# Delay: ', post_delay.total_seconds())
print('# Links: ', links.len())
print('# Enter to stop, L to reload')

keepGoing = True
while(keepGoing):   
    
    if msvcrt.kbhit():
        key = msvcrt.getch().decode('utf-8')        
        if key == '\r' or key == '\n':
            break
        elif key == 'l':
            print("> reloading links")
            links.load()

    url, title, subreddit = links.get_random()
    subreddit = reddit.subreddit(subreddit)    
    ret = subreddit.submit(title, url=url)    
    print("{} Posting in {} - {} >>> {}".format(datetime.datetime.now(), subreddit, title, ret))    
    time.sleep(post_delay.total_seconds())    
    

print("> End")
