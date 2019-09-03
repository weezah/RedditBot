import praw
import time
import datetime
import threading
import links
import msvcrt
from enum import IntEnum
from config import Config


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

        if not config.debug:
            if link_type == "url":
                subreddit.submit(title, url=content)
            elif link_type == "image":
                subreddit.submit_image(title, content, timeout=20)
            elif link_type == "video":
                subreddit.submit_video(title, content, timeout=25)
            else:
                print("Unknown link_type: ", link_type)

        print("{} Posting in {} - {}".format(
            datetime.datetime.now(), sr, title))


def random_post():
    global keepGoing
    while(keepGoing):
        link_type, content, title, sr = links.get_random()
        try:
            post(link_type, content, title, sr)
        except praw.exceptions.APIException as err:
            print(err)
        finally:
            time.sleep(config.post_delay.total_seconds())


def sequential_post():
    global keepGoing
    for i in range(links.len()):
        current = links.data[i]
        for r in links.data[i]["subreddits"]:
            title = links.get_random_title(i)
            content = links.get_random_content(i)
            link_type = links.get_type(i)

            try:
                post(link_type, content, title, r)
            except praw.exceptions.APIException as err:
                print(err)
            finally:
                time.sleep(config.post_delay.total_seconds())
    keepGoing = False


# main
keepGoing = True
config = Config()
reddit = praw.Reddit(config.praw_profile)
links = links.Links(config.json_file)

print(config)
print('# Links found: ', links.len())
print('# Enter to stop, L to reload')

x = threading.Thread(target=thread_check_key)
x.start()

if config.random_posts:
    random_post()
else:
    sequential_post()
