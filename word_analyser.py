import coeffieient_body_analyser
import wordcloud_examples
import tweet_geter
import logging
import dictionary
import matplotlib.cm as cm
import matplotlib.colors as mcolors


class WordAnalyser():
    def __init__(self, mysql = None, mecab = None):
        self.mecab = coeffieient_body_analyser.CoeffieientBodyAnalyser()
        self.wordcloud = wordcloud_examples.WordCloudExamples()
        self.tweet = tweet_geter.TweetGeter()
        self.dict = dictionary.Dictionary()

    def analyse(self, word, userid):
        tweet_data = self.tweet.extract_tweet(word)
        sentence = ""
        for tweet_dict in tweet_data:
            sentence = sentence + tweet_dict[1]
        elements = self.mecab.exe_mecab(sentence)
        print(elements)
        feeling_counter = self.dict.judge(elements[0])
        if feeling_counter["n"] == 0: 
            feeling = 1
        else: 
            feeling = feeling_counter["p"] / feeling_counter["n"]
        self.wordcloud.exe_wordcloud(elements[1], word, userid, feeling)
        logging.debug(elements)

#全体的にメソッド、クラス名が抽象度が高い名前なので、メソッドから何してる処理なのか、分かりづらい。もう少し、工夫すると、メソッドが増えるかもしれないし、処理がわかりやすく。
#りファクターの機能を使う
#発表時間15分