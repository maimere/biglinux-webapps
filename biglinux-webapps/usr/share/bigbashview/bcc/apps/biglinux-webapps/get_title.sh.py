#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import requests
import re
from bs4 import BeautifulSoup

def get_title(url):

    headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5)'
    'AppleWebKit/537.36 (KHTML, like Gecko)'
    'Chrome/50.0.2661.102 Safari/537.36'
    }

    try:
        resp = requests.get(url, headers=headers, timeout=10)
    except:
        return

    if resp.status_code >= 400: return

    try:
        soup = BeautifulSoup(resp.text, features='html.parser')
        html_title = soup.title.string.strip().encode('latin-1').decode('utf-8')
        title = re.sub(r'[^\w]',' ', html_title)
        _title = re.sub(r'\s+',' ', title)
        print(_title, end='')

    except UnicodeEncodeError as e:
        html_title = soup.title.string.strip()
        title = re.sub(r'[^\w]',' ', html_title)
        _title = re.sub(r'\s+',' ', title)
        print(_title, end='')

    else:
        return

url = sys.argv[1].strip()
if 'http' not in url:
    url = 'https://'+url
get_title(url)
