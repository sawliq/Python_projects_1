import tweepy
import time

auth = tweepy.OAuthHandler('iF5tcsgYoK4IXF8hdUM0Rl2nf', 'lXB55zeWWi2E0ZCTVNOiUp6YtoqaVSDIYQxff8ddZNdU9DiHTk')
auth.set_access_token('1140637077542821888-4tA8dWuguMibW7jzXZXTPp00iWTgeG', 'RFq4PJibhny7xuWk5eKN0IDd9r8nVibCphN06st81FJEs')

api = tweepy.API(auth)
user=api.me()


def limit_handler(Cursor):
    try:
        while True:
            yield Cursor.next()
    except tweepy.RateLimitError:
        time.sleep(300)

for follwer in tweepy.Cursor(api.followers).items( ):
   if follwer.name =='Aysha Sariya':
     follwer.follow()
     break