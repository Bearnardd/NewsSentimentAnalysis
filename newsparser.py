#!/usr/bin/env python3

import requests

class NewsParser:
  def __init__(self):
    self._titles = []
    self._desc = []
    self._content = []

  def get_data(self, topic, page_size):
    self._url = f'https://newsapi.org/v2/everything?q={topic}' \
                '&apiKey=0fce127066fb4adda75f524c202905eb' \
                f'&pageSize={page_size}'
    self._response = requests.get(self._url)
    for page in range(page_size):
      title = self._response.json()['articles'][page]['title']
      desc = self._response.json()['articles'][page]['content']
      content = self._response.json()['articles'][page]['content']
      self._titles.append(title)
      self._desc.append(desc)
      self._content.append(content)



   

    

