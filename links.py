import json
from random import randrange
from random import choice

class Links(object):   

    def __init__(self):
        self.load()
        self.last_url = -1
        self.last_title = -1
        self.last_subreddit = -1
        self.last_link = -1
    
    def load(self):
        with open("links.json", "r") as read_file:
            self.data = json.load(read_file)    

    def get_link(self, idx):
        title_idx = self.random_not(self.last_title, len(self.data[idx]["titles"]))
        self.last_title = title_idx
        title = self.data[idx]["titles"][title_idx]
        
        url_idx = self.random_not(self.last_url, len(self.data[idx]["url"]))
        self.last_url = url_idx
        url = self.data[idx]["url"][url_idx]

        subreddit_idx = self.random_not(self.last_subreddit, len(self.data[idx]["subreddits"]))
        self.last_subreddit = subreddit_idx
        subreddit = self.data[idx]["subreddits"][subreddit_idx]
        return url, title, subreddit

    def get_random(self):
        idx = self.random_not(self.last_link, self.len()) 
        self.last_link = idx       
        return self.get_link(idx)

    def len(self):
        return len(self.data)

    def random_not(self, last, count):
        if count <= 1:
            return choice([i for i in range(0, count)])
        else:
            return choice([i for i in range(0, count) if i not in [last]])

print(Links().get_random())
