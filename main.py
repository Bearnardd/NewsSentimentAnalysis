#!/usr/bin/env python3

'''
TODO:
 - add database and fill news
 - figure out how to label news
 - build neural network
 - clean code
'''


from newsparser import NewsParser
import glob
import numpy as np
import pandas as pd
import os

np.random.seed(2)

''
data_dir = os.path.join(os.getcwd(), 'data/train')
def get_data(folder_name, pos=True):
  text = []
  file_list = glob.glob(os.path.join(data_dir, folder_name, '*.txt'))
  for file_path in file_list:
    with open(file_path, 'r') as f:
      text.append(f.read())
  df = pd.DataFrame(columns=['text', 'label'])
  df['text'] = text
  if pos:
    df['label'] = np.ones(len(text))
  else:
    df['label'] = np.zeros(len(text))
  return df

def concat_df(dfs, shuffle=True):
  data = pd.concat(dfs)
  if shuffle:
    data = data.sample(frac=1).reset_index(drop=True)
  else:
    data = data.reset_index(drop=True)
  return data

path = '/home/bartek/Desktop/Projects/Python/NewsSentimentAnalysis/data/news.db'
topics = ['Love', 'Hate', 'Kill', 'Happy']
labels = [True, False, False, True]
if __name__ == '__main__':
  df_pos = get_data('pos', True)
  df_neg = get_data('neg', False)
  data = concat_df([df_pos, df_neg])
  print(data.sample(5))
  '''
  parser = NewsParser()
  parser.connect_to_db(path)
  for topic, label in zip(topics, labels):
    parser.get_data(topic, label, 5, True)
  parser.disconnect()
  print('DONE!')
  '''



