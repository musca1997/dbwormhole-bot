import doubanrobot
from bs4 import BeautifulSoup
import requests
import time
import os
import random

email=  'PUT EMAIL HERE'
dou_password = 'PUT PASS HERE'

def get_thing():
    i = random.randint(1000001, 30333333)
    douban_url = 'https://www.douban.com/thing/' + str(i)
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
    group_description = soup.find('div', attrs={"class": "intro"})

    text = ''
    if group_description is not None:
        group_description = group_description.get_text()
        for i in group_description:
            text = text + i
    group_data = group_title + '\n' + douban_url + '\n' + text
    group_data = group_data.replace('https://', '')
    print group_data
    app = doubanrobot.DoubanRobot(email, dou_password)
    app.talk_status(group_data)
    time.sleep(3600)
    get_group()

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
        group_description = group_description.get_text()
        for i in group_description:
            text = text + i
    group_data = group_title + '\n' + douban_url + '\n' + text
    group_data = group_data.replace('https://', '')
    print group_data
    app = doubanrobot.DoubanRobot(email, dou_password)
    app.talk_status(group_data)
    time.sleep(3600)
    get_site()

def get_site():
    i = random.randint(100027, 300999)
    douban_url = 'https://site.douban.com/'+ str(i)
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
    group_description = soup.find('div', attrs={"class": "desc"})

    text = ''
    if group_description is not None:
        group_description = group_description.get_text()
        for i in group_description:
            text = text + i
    group_data = group_title + '\n' + douban_url + '\n' + text
    group_data = group_data.replace('https://', '')
    print group_data
    app = doubanrobot.DoubanRobot(email, dou_password)
    app.talk_status(group_data)
    time.sleep(3600)
    get_list()

def get_list():
    i = random.randint(10010, 99999)
    douban_url = 'https://www.douban.com/doulist/' + str(i)
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:27.0) Gecko/20100101 Firefox/27.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'q=0.8,en-us;q=0.5,en;q=0.3',
            'Accept-Encoding': 'gzip, deflate',
            'DNT': '1',
            'Connection': 'keep-alive'}

    r = requests.get(douban_url, headers=headers)
    if not (r.status_code == 200):
        print "nope!!!!"
        return
    soup = BeautifulSoup(r.content,"html.parser")
    group_title = soup.title.string
    group_description = soup.find('div', attrs={"class": "doulist-about"})

    text = ''
    if group_description is not None:
        group_description = group_description.get_text()
        for i in group_description:
            text = text + i
    group_data = group_title + '\n' + douban_url + '\n' + text
    group_data = group_data.replace('https://', '')
    app = doubanrobot.DoubanRobot(email, dou_password)
    app.talk_status(group_data)
    time.sleep(3600)


if __name__ == '__main__':
    while True:
        get_thing()
