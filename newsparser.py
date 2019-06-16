#!/usr/bin/env python3

import requests
import sqlite3
from keras.models import load_model
from cleaner import Cleaner
from keras.preprocessing.text import Tokenizer


class NewsParser:
  def __init__(self):
    pass


  def get_data(self, topic, page_size, database=True):
    self.titles = []
    self.desc = []
    self.content = []
    url = f'https://newsapi.org/v2/everything?q={topic}' \
                '&apiKey=0fce127066fb4adda75f524c202905eb' \
                f'&pageSize={page_size}'
    response = requests.get(url)
    for page in range(page_size):
      title = response.json()['articles'][page]['title']
      desc = response.json()['articles'][page]['description']
      content = response.json()['articles'][page]['content']

      self.titles.append(title)
      self.desc.append(desc)
      self.content.append(content)
  






   

    

