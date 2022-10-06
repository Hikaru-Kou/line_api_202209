# ライブラリのインポート
import tweepy
from datetime import datetime,timezone
import pytz
import os

import enviroment_editor

class TweetGeter():
    #initで設定してあげる↓
    enviroment_editor.EnviromentEditor()
    def extract_tweet(self, word):
        self.word = word
        #initに入れる↓
        # Twitterの認証(アカウント情報を入力)、環境変数で設定してください
        consumer_key        = os.getenv('consumer_key')
        consumer_secret     = os.getenv('consumer_secret')
        access_token        = os.getenv('consumer_token')
        access_token_secret = os.getenv('consumer_token_secret')

        #Twitterの認証
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        api = tweepy.API(auth)

        #　”wait_on_rate_limit = True”　利用制限にひっかかた時に必要時間待機する
        api=tweepy.API(auth,wait_on_rate_limit=True)


        # 検索条件の設定
        search_word = self.word
        #何件のツイートを取得するか
        item_number = 100
        #検索条件を元にツイートを抽出
        tweets = tweepy.Cursor(api.search_tweets,q=search_word, tweet_mode='extended',result_type="mixed",lang='ja').items(item_number)

        #抽出したデータから必要な情報を取り出す
        #取得したツイートを一つずつ取り出して必要な情報をtweet_dataに格納する
        tw_data = []

        for tweet in tweets:

            #tweet_dataの配列に取得したい情報を入れていく
            tw_data.append([
                tweet.id,
                tweet.full_text,
                #tweet.favorite_count, 
                #tweet.retweet_count, 
                #tweet.user.id, 
                #tweet.user.screen_name,
                #tweet.user.name,
                #tweet.user.description,
                #tweet.user.friends_count,
                #tweet.user.followers_count,
                #tweet.user.following,
                #tweet.user.profile_image_url,
                #tweet.user.profile_background_image_url,
                #tweet.user.url
                            ])

        return tw_data
        