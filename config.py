import argparse
import datetime

class Config:
    def __init__(self):
        args = self.parse_args()
        self.json_file = args.json
        self.praw_profile = args.praw
        self.random_posts = args.random
        self.post_delay = args.delay
        self.debug = args.test

    def __repr__(self):
        return '''
Config:
> json:\t\t%s
> praw profile:\t%s
> random mode:\t%s
> post delay:\t%s
> debug mode:\t%s
''' % (repr(self.json_file),
            repr(self.praw_profile),
            repr(self.random_posts),
            repr(self.post_delay),
            repr(self.debug))

    def parse_args(self):

        defaults = {
            "post_delay": datetime.timedelta(minutes=30),
            "random_posts": False,
            "debug": False,
            "praw_profile": "bot"
        }

        parser = argparse.ArgumentParser()
        parser.add_argument("-j", "--json",
                            help="json links file path", required=True)

        parser.add_argument("-d", "--delay",
                            help="delay between posts in seconds",
                            type=int, required=False,
                            default=defaults['post_delay'])

        parser.add_argument("-t", "--test",
                            help="test mode",
                            action='store_true' if not defaults['debug'] else 'store_false')

        parser.add_argument("-r", "--random",
                            help="random mode / sequential mode",
                            action='store_true' if not defaults['random_posts'] else 'store_false')

        parser.add_argument("-p", "--praw",
                            help="praw profile name",
                            required=False,
                            default=defaults['praw_profile'])

        

        return parser.parse_args()
