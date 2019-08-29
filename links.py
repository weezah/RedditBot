import json
import random

class Links(object):   

    def __init__(self):
        self.load()
    
    def load(self):
        with open("links.json", "r") as read_file:
            self.data = json.load(read_file)    

    def get_link(self, idx):
        title = random.choice(self.data[idx]["titles"])
        url = random.choice(self.data[idx]["url"])
        subreddit = random.choice(self.data[idx]["subreddits"])
        return url, title, subreddit

    def get_random(self):
        idx = random.randrange(0, self.len())
        return self.get_link(idx)

    def len(self):
        return len(self.data)



#print(Links().get_link(0))
