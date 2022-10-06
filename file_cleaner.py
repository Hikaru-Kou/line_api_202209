import datetime
import os
 
now = datetime.datetime.now()# 現在の日付を取得
print(now)
#os.chdir()カレントは好きなところを選んでください。
os.chdir("./static")
for file in os.listdir():
    mtime = datetime.datetime.fromtimestamp(os.path.getatime(file))
    #base, ext = os.path.splitext(file)
    if (now - mtime).seconds >= 300: # 5分以上経過している場合は削除
        os.remove(file)