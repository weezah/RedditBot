import praw
import time
import datetime
import links
import msvcrt
from enum import IntEnum

#config
post_delay = datetime.timedelta(minutes=30)
file_path = "links.json"

links = links.Links(file_path)
reddit = praw.Reddit('bot')

print('# Delay: ', post_delay.total_seconds())
print('# Links: ', links.len())
print('# Enter to stop, L to reload')

keepGoing = True
while(keepGoing):   
    
    #todo put this in a separate thread
    if msvcrt.kbhit():
        key = msvcrt.getch().decode('utf-8')        
        if key == '\r' or key == '\n':
            break
        elif key == 'l':
            print("> reloading links")
            links.load()
            
    #post        
    link_type, content, title, subreddit = links.get_random()
    subreddit = reddit.subreddit(subreddit)

    if link_type == "url":
        subreddit.submit(title, url=content)
    elif link_type == "image":
        subreddit.submit_image(title, content, timeout=20)
    elif link_type == "video":
        subreddit.submit_video(title, content, timeout=25)
    else:
        print("Unknown link_type: ", link_type)

    print("{} Posting in {} - {}".format(datetime.datetime.now(), subreddit, title))
    time.sleep(post_delay.total_seconds())

print("> End")
