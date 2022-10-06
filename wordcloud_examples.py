# ライブラリのインポート
from wordcloud import WordCloud
from wordcloud import STOPWORDS
import dictionary
import matplotlib.cm as cm
import matplotlib.colors as mcolors

class WordCloudExamples():
    def __init__(self, mysql = None, mecab = None):
        self.dict = dictionary.Dictionary()

    def exe_wordcloud(self, text, exclusion, userid, feeling):
        self.feeling = feeling
        color = self.select_backgound()
        # 除外ワード指定
        WordCloudExamples.exclude(self,exclusion)
        # ワードクラウドの作成
        wordcloud = WordCloud(background_color = color, color_func = self.dict.select, font_path = '/home/intern3/fonts/Arial Unicode.ttf').generate(text)
        # 画像保存
        wordcloud.to_file('./static/' + userid)

        

    def exclude(self,exclusion):
        STOPWORDS.add('https')
        STOPWORDS.add('co')
        STOPWORDS.add('RT')
        STOPWORDS.add('t')
        STOPWORDS.add(exclusion)
        STOPWORDS.add('ん')
        STOPWORDS.add('の')

    def select_backgound(self):
        if self.feeling >= 0.5:
            return "white"
        
        else:
            return "black"

