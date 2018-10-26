import doubanrobot
from bs4 import BeautifulSoup
import requests
import time
import os
import random

email=  'PUT EMAIL HERE'
dou_password = 'PUT PASS HERE'

def get_group():
    i = random.randint(10001, 640099)
    douban_url = 'https://www.douban.com/group/'+ str(i)
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:27.0) Gecko/20100101 Firefox/27.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'q=0.8,en-us;q=0.5,en;q=0.3',
            'Accept-Encoding': 'gzip, deflate',
            'DNT': '1',
            'Connection': 'keep-alive'}

    r = requests.get(douban_url, headers=headers)
    if not (r.status_code == 200):
        return
    soup = BeautifulSoup(r.content,"html.parser")
    group_title = soup.title.string
    group_description = soup.find('div', attrs={"class": "group-intro"})

    text = ''
    if group_description is not None:
        group_description = group_description.get_text().strip().replace(' ', '\n')
        for i in group_description:
            text = text + i
    group_data = group_title + '\n' + douban_url + '\n' + text

    app = doubanrobot.DoubanRobot(email, dou_password)
    app.talk_status(group_data)
    time.sleep(3600)



if __name__ == '__main__':
    while True:
        get_group()
