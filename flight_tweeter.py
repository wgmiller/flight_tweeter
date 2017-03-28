import config, tweepy, json
from datetime import datetime, timedelta
from sky_picker import SkyPickerApi


class flight_tweeter:
    def __init__(self):
        #config = yaml.safe_load(open('config.yaml').read())
        auth = tweepy.OAuthHandler(config.CONSUMER_KEY, config.CONSUMER_SECRET)
        auth.set_access_token(config.ACCESS_KEY, config.ACCESS_SECRET)
        self.api = tweepy.API(auth)
        self.get_flights()
    
    def tweet_tester(self):
        tweet = 'passed test for: ' + datetime.now().strftime('%m/%d/%y %H:%M')
        try:
            self.api.update_status(tweet)
        except tweepy.error.TweepError:
            print('tweepy error')
        return tweet

            
    def tweet_cheapest(self):
        tweet = 'The cheapest flight to Europe in 4 weeks (' + self.day + ') is only $'
        p = self.sp_results[0]
        tweet += str(p['price']) + '! ' + p['legs'][0]['from'] + ' to ' + p['legs'][0]['to']
        #self.api.update_status(tweet)
        try:
            self.api.update_status(tweet)
        except tweepy.error.TweepError:
            print('tweepy error')
        return tweet

    def get_flights(self):
        t = datetime.now() + timedelta(days=28)
        self.day = t.strftime('%m/%d')
        travel_date = t.strftime('%m/%d/%Y')
        date = datetime.strptime(travel_date, '%m/%d/%Y')
        origin = 'US'
        destination = '48.41-7.96-1779km'
        num_adults = '1'
        sp_api = SkyPickerApi()
        self.sp_results = sp_api.search_flights(origin, destination, date, date, int(num_adults),0)

    def print_flights(self, max):
        results = self.get_flights()
        for p in sp_results[:max]:
            tweet = 'The cheapest flight to Europe in 4 weeks is only $'
            tweet += str(p['price']) + '! ' + p['legs'][0]['from'] + ' to ' + p['legs'][0]['to']
            print(tweet)        
