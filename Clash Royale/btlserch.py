# G0Q9P2UJ2
# PLLJRRY2

import requests
from bs4 import BeautifulSoup
import os
import datetime
import schedule
import time

tol = None
current = None

# コンソールタグ入力
playertag = input("プレイヤータグを入力してください：")

target_url = 'https://royaleapi.com/player/' + playertag + '/battles'

# 最新のバトルを取得
def job():
    global tol
    global current
    # html情報取得
    r = requests.get(target_url)
    soup = BeautifulSoup(r.text, 'lxml')
    
    # 最新のトロフィーを取得
    current = soup.find_all(class_='detail')[0].text
    current.replace( '\n' , '' )
    
    if (not tol or current == tol):
        print(str(datetime.datetime.now().strftime('%Y年%m月%d日%H時%M分')) + "：" + current)
        tol = current
    else:
        tol = current
        # 通知システム
        message = '対戦が更新されました！'
        os.system("osascript -e 'display dialog\" {}\"'".format(message))
    
schedule.every(10).minutes.do(job)
        
while True:
    schedule.run_pending()