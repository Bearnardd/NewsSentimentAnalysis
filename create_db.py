#!/usr/bin/env python3

import sqlite3


path = '/home/bartek/Desktop/Projects/Python/NewsSentimentAnalysis/data/news.db'

def create_news_db(path):
  conn = sqlite3.connect(path)
  c = conn.cursor()
  c.execute('CREATE TABLE IF NOT EXISTS news(title TEXT, description TEXT, content TEXT)')
  try:
    c.execute('ALTER TABLE news ADD COLUMN label TEXT')
  except:
    pass
  conn.commit()
  conn.close()

  

if __name__ == '__main__':
  create_news_db(path)
  















