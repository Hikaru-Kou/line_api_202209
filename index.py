# Python 3.10.4
# Flask 2.1.2
# Flaskの公式ドキュメント：https://flask.palletsprojects.com/en/2.0.x/
# python3の公式ドキュメント：https://docs.python.org/ja/3.9/
# python3の基礎文法のわかりやすいサイト：https://note.nkmk.me/python/
# 使用するモジュールのインポート
# pythonが提供しているモジュールのインポート
import json
import logging
import requests
from flask import Flask, request
from flask import send_file, Response
import os
# 自分で作成したモジュールのインポート
import word_analyser
import time
import hashlib

# Flaskクラスをnewしてappに代入
# gunicornの起動コマンドに使用しているのでここは変更しないこと
app = Flask(__name__)

# ログの設定
format = "%(asctime)s: %(levelname)s: %(pathname)s: line %(lineno)s: %(message)s"
logging.basicConfig(filename='/var/log/intern3/flask.log', level=logging.DEBUG, format=format, datefmt='%Y-%m-%d %H:%M:%S')


# 「/」にPOSTリクエストが来た場合、index関数が実行される
@app.route('/', methods=['post'])
def index():
    os.environ['MECABRC'] = "/etc/mecabrc"
    analiser = word_analyser.WordAnalyser()
    # 以下のコードでログを出力できる。出力先は「ログの設定」にあるファイル。コマンドラインに出力する場合はprintを使う。
    logging.debug("こんにちは!")
    # POSTリクエストのbodyを取得
    body_binary = request.get_data()
    body = json.loads(body_binary.decode())
    url_items = "https://api.line.me/v2/bot/message/reply"
    replytoken = body['events'][0]["replyToken"]
    userid = body['events'][0]['source']['userId'] + '.jpg'
    logging.debug(userid)
    stamp =  hashlib.md5(str(int(time.time())).encode()).hexdigest()+ ".jpg"
    analiser.analyse(body['events'][0]['message']['text'], stamp)
    headers = { 
         'Content-Type': "application/json",
         'Authorization': "Bearer fQx5PH8M40meuh6MeVte+sekxFOW5wY05UopOL8CsgJmCyZd6eU7TDD0MeCYFWvjX2Rj8q7ELTYVaL5dHxyVhUQj4TYgulfs2X+D+qOkKNWt/+dCABxVs1IonvvzKM1aDpHZT2jZaQKyGU4087LZJgdB04t89/1O/w1cDnyilFU="
                 }
    
    term = {
         'replyToken': replytoken,
         'messages': [{
             'type': 'image',
             "originalContentUrl": "https://intern3-term3.tobila-techintern.com/static/" + stamp,
             "previewImageUrl": "https://intern3-term3.tobila-techintern.com/static/" + stamp
         }]
     }
    logging.debug(term)
    
    response = requests.post(url_items, headers = headers, data = json.dumps(term))

    if not response.status_code == 200:
        logging.debug("response error: " + str(response.status_code) + 
                      "::::返信に失敗しました。ソースコードを見直してください")

        response = response.json()
        for key in response:
            logging.debug("error {}::::{}".format(key ,response[key]))

    return Response(response=json.dumps({'message': 'Success sent all responce'}), status=200)
