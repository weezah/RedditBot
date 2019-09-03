import json
from random import randrange
from random import choice


class Links:

    def __init__(self, file_path):
        self.last_subreddit = -1
        self.last_link = -1
        self.file_path = file_path
        self.load()
    
    def load(self):
        with open(self.file_path, "r") as read_file:
            self.data = json.load(read_file)

    def get_link(self, idx):
        link_type = self.get_type(idx)
        title = self.get_random_title(idx)
        content = self.get_random_content(idx)
        subreddit = self.get_random_subreddit(idx)
        return link_type, content, title, subreddit

    def get_type(self, idx):
        return self.data[idx]["type"]

    def get_random_subreddit(self, idx):
        last_subreddit = -1 if "last_subreddit" not in self.data[idx] else self.data[idx]["last_subreddit"]
        subreddit_idx = self.random_not(last_subreddit, len(self.data[idx]["subreddits"]))
        self.data[idx]["last_subreddit"] = subreddit_idx
        return self.data[idx]["subreddits"][subreddit_idx]

    def get_random_content(self, idx):
        last_content = -1 if "last_content" not in self.data[idx] else self.data[idx]["last_content"]
        content_idx = self.random_not(last_content, len(self.data[idx]["content"]))
        self.data[idx]["last_content"] = content_idx
        return self.data[idx]["content"][content_idx]

    def get_random_title(self, idx):
        last_title = -1 if "last_title" not in self.data[idx] else self.data[idx]["last_title"]
        title_idx = self.random_not(last_title, len(self.data[idx]["titles"]))
        self.data[idx]["last_title"] = title_idx
        return self.data[idx]["titles"][title_idx]

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
