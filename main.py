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
import numpy as np
import os
    
data_dir = os.path.join(os.getcwd(), 'data/imdb_master.csv')
dow_path = '/home/bartek/Downloads/'
glove_dir = os.path.join(dow_path, 'glove.6B.50d.txt')

def get_data(path):
  data = pd.read_csv(path, encoding='latin-1')
  data = data.drop(['Unnamed: 0', 'type', 'file'], axis=1)
  data = data[data.label != 'unsup']
  data = data.reset_index(drop=True)
  data['label'] = data.label.map({'neg':0, 'pos':1})
  return data

def loadGloveModel(glove_dir):
  '''
  Loads glove weigths from
  from downloaded file
  '''
  print('Loading Glove Model!')
  model = {}
  with open(glove_dir, 'r') as f:
    for line in f:
      splitline = line.split()
      word = splitline[0]
      embedding = np.array([float(val) for val in splitline[1:]])
      model[word] = embedding
  print(f'Done! {len(model)} words loaded')
  return model



def create_emb_matrix(emb_idx, tokenizer, emb_size):
    word_idx = tokenizer.word_index
    lenght = min(max_words, len(word_idx))
    all_embeddings = np.stack(emb_idx.values())
    mean = all_embeddings.mean()
    std = all_embeddings.std()
    embedding_matrix = np.random.normal(mean, std, (lenght, emb_size))
    for word, val in word_idx.items():
        if val >= max_words:
            continue
        embedding_vector = emb_idx.get(word)
        if embedding_vector is not None:
            embedding_matrix[val] = embedding_vector
    return embedding_matrix



path = '/home/bartek/Desktop/Projects/Python/NewsSentimentAnalysis/data/news.db'
topics = ['Love', 'Hate', 'Kill', 'Happy']
labels = [True, False, False, True]
if __name__ == '__main__':
  loadGloveModel(glove_dir)

  










  
  










  ''' 

  parser = NewsParser()
  parser.connect_to_db(path)
  for topic, label in zip(topics, labels):
    parser.get_data(topic, label, 5, True)
  parser.disconnect()
  print('DONE!')
  '''



