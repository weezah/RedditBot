import praw
import time
import datetime
import threading
import links
import msvcrt
from enum import IntEnum


# config
post_delay = datetime.timedelta(minutes=30)
file_path = "matt.json"
random_posts = False
debug = True
keepGoing = True
links = links.Links(file_path)
reddit = praw.Reddit('bot')

print('# Delay: ', post_delay.total_seconds())
print('# Links: ', links.len())
print('# Random: ', random_posts)
print('# Debug: ', debug)
print('# Enter to stop, L to reload')


def thread_check_key():
    global keepGoing
    global links
    while(keepGoing):
        if msvcrt.kbhit():
            key = msvcrt.getch().decode('utf-8')        
            if key == '\r' or key == '\n':
                keepGoing = False
                exit()                
            elif key == 'l':
                print("> reloading links")
                links.load()


def post(link_type, content, title, sr):
        subreddit = reddit.subreddit(sr)

        if not debug:
            if link_type == "url":
                print("Unknown link_type: ", link_type)
                subreddit.submit(title, url=content)
            elif link_type == "image":
                print("Unknown link_type: ", link_type)
                subreddit.submit_image(title, content, timeout=20)
            elif link_type == "video":
                subreddit.submit_video(title, content, timeout=25)
            else:
                print("Unknown link_type: ", link_type)

        print("{} Posting in {} - {}".format(datetime.datetime.now(), sr, title))


def random_post():
    global keepGoing
    while(keepGoing):
        post(links.get_random())
        time.sleep(post_delay.total_seconds())


def sequential_post():
    global keepGoing
    for i in range(links.len()):
        current = links.data[i]
        for r in links.data[i]["subreddits"]:
            title = links.get_random_title(i)
            content = links.get_random_content(i)
            link_type = links.get_type(i)
            post(link_type, content, title, r)
    keepGoing = False


# main
x = threading.Thread(target=thread_check_key)
x.start()

if random_posts:
    random_post()
else:
    sequential_post()
