#!/usr/bin/env python3

'''
  TODO:
   - add database and fill news
 - figure out how to label news
 - build neural network
 - clean code
'''


from newsparser import NewsParser
from cleaner import Cleaner
import pandas as pd
import os

data_dir = os.path.join(os.getcwd(), 'data/imdb_master.csv')

def get_data(path):
  data = pd.read_csv(path, encoding='latin-1')
  data = data.drop(['Unnamed: 0', 'type', 'file'], axis=1)
  data = data[data.label != 'unsup']
  data = data.reset_index(drop=True)
  data['label'] = data.label.map({'neg':0, 'pos':1})
  return data

def loadGloveModel(glove_dir):
  print('Loading Glove Model')
  model = {}
  with open(glove_dir, 'r') as f:
    for line in f:
      splitline = line.split()
      word = splitline[0]
      embedding = np.array([float[val] for val in splitline[1:])
      model[word] = embedding
  print(f'Done! {len(model)} words loaded')
  return model

path = '/home/bartek/Desktop/Projects/Python/NewsSentimentAnalysis/data/news.db'
topics = ['Love', 'Hate', 'Kill', 'Happy']
labels = [True, False, False, True]
if __name__ == '__main__':
  data = get_data(data_dir)
  cleaner = Cleaner(data)
  cleaner.create_dataset('review', False)
  cleaner.normalize()
  print(cleaner.text[10])











  
  










  ''' 

  parser = NewsParser()
  parser.connect_to_db(path)
  for topic, label in zip(topics, labels):
    parser.get_data(topic, label, 5, True)
  parser.disconnect()
  print('DONE!')
  '''



