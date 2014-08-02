"""Gets data from twitter.

Collects tweets, usually English, by searching for random stop words (i.e.
normal everyday words like "that", "which", "and").

You'll need a Twitter API key for that.

This isn't currently a command line program -- you'll need to change variables
in the code itself.
"""

from TwitterAPI import TwitterAPI
from getpass import getpass
from sklearn.feature_extraction.stop_words import ENGLISH_STOP_WORDS as stop_words
from random import choice


num_to_get = 10000
stop_words = list(stop_words)

access_key = # Put your Twitter API information here
access_secret = # And here
consumer_key = # and here
consumer_secret = # and here!

api = TwitterAPI(consumer_key=consumer_key, consumer_secret=consumer_secret,
                    access_token_key=access_key, access_token_secret=access_secret)
                    
c = 0
for i in range(int(num_to_get / 10)):
	word = choice(stop_words)
	r = api.request('search/tweets', {'q': word})
	for item in r.get_iterator():
		c += 1
		if c > num_to_get: break
		try:
			print(repr(item['text']))
		except:
			pass
