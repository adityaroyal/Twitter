import simplejson

tweets_data_path = 'twitter_data.txt'

tweets_data = []
tweets_file = open(tweets_data_path, "r")

for line in tweets_file:
    try:
        tweet = simplejson.loads(line)
        tweets_data.append(tweet)
    except:
        continue

import pandas as pd
tweets = pd.DataFrame()
tweets['text'] = map(lambda tweet: tweet['text'], tweets_data)

# this code WORKS
import tornado.escape
import unirest
mashape_nlp = "https://loudelement-free-natural-language-processing-service.p.mashape.com/nlp-text/?text="

rows_list = []
for row in range(len(tweets)):
    trythistext = tweets["text"][row]
    nlp_api_url = mashape_nlp + tornado.escape.url_escape(trythistext)
    response = unirest.get(nlp_api_url, headers =
        {
        "X-Mashape-Key": "JMFcUeZ6TdmshCn7hG65rLpnuNXLp1Dhx4EjsnVBpPFCi6hWZ0",
        "Accept": "application/json"
        }
    )
    dict1 = {'category': response.body["sentiment-text"], 'score': response.body["sentiment-score"]}
    rows_list.append(dict1)

sentiment_df = pd.DataFrame(rows_list)

# output data frame to csv
sentiment_df.to_csv('output.csv')
