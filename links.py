import json
import random

class Links(object):   

    def __init__(self):
        with open("links.json", "r") as read_file:
            self.data = json.load(read_file)    

    
    def get_link(self, idx):
        title = random.choice(self.data[idx]["titles"])
        url = self.data[idx]["url"]
        subreddit = random.choice(self.data[idx]["subreddits"])
        return url, title, subreddit

    def len(self):
        return len(self.data)



#print(Links().get_link(0))
