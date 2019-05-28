#!/usr/bin/env python3

import requests
import sqlite3

class NewsParser:
  def __init__(self):
    self._titles = []
    self._desc = []
    self._content = []

  def connect_to_db(self, path):
    self._conn = sqlite3.connect(path)
    self._c = self._conn.cursor()

  def disconnect(self):
    return self._conn.close()

  def get_data(self, topic, positive, page_size, database=True):
    self._url = f'https://newsapi.org/v2/everything?q={topic}' \
                '&apiKey=0fce127066fb4adda75f524c202905eb' \
                f'&pageSize={page_size}'
    self._response = requests.get(self._url)
    for page in range(page_size):
      title = self._response.json()['articles'][page]['title']
      desc = self._response.json()['articles'][page]['description']
      content = self._response.json()['articles'][page]['content']
      self._titles.append(title)
      self._desc.append(desc)
      if positive:
        label = 1
      else:
        label = 0
      self._content.append(content)
      if database:
        self._c.execute('INSERT INTO news VALUES(?, ?, ?, ?)', (title, desc, content, label))
        self._conn.commit()






   

    

