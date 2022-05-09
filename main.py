import tweepy


def get_info(credential):
    with open('/home/jezze/Documents/VS Projects/Tweepy bot/keys.txt') as f:
        lines = f.readlines()
        for line in lines:
            if credential in line:
                return line.split("= ",1)[1]



auth = tweepy.OAuth1UserHandler(get_info('Api_keys').strip(), get_info('API_secret_key').strip())
auth.set_access_token(get_info('Access_token').strip(), get_info('access_secret').strip())
api = tweepy.API(auth)
try:
    api.verify_credentials()
    print('Works!!')
except:
    print('Problem')
timeline = api.home_timeline()
user = api.get_user(screen_name="jdogster")
api.create_friendship(user_id=user.id)
user_timeline = api.user_timeline(user_id=user.id, count=200, include_rts=False, tweet_mode='extended')
for tweet in user_timeline:
    api.create_favorite(tweet.id)
    api.retweet(tweet.id)
