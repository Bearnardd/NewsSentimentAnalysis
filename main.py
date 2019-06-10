#!/usr/bin/env python3

'''
  TODO:
   - add database and fill news
 - figure out how to label news
 - build neural network
 - clean code
'''


from newsparser import NewsParser
from network import Network
from cleaner import Cleaner
from keras.preprocessing.text import Tokenizer
from sklearn.model_selection import train_test_split
from keras.preprocessing.sequence import pad_sequences
import pandas as pd
import numpy as np
import os
import warnings
warnings.filterwarnings('ignore')
    
data_dir = os.path.join(os.getcwd(), 'data/imdb_master.csv')
dow_path = '/home/bartek/Downloads/'
glove_dir = os.path.join(dow_path, 'glove.6B.50d.txt')
maxlen = 130
max_words = 10000
emb_size = 128 

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
  cleaner = Cleaner()
  df = get_data(data_dir)  
  df['processed_reviews'] = df.review.apply(lambda x: cleaner.clean_data(x))

  tokenizer = Tokenizer(max_words)
  tokenizer.fit_on_texts(df['processed_reviews'])
  list_tokenizer_train = tokenizer.texts_to_sequences(df['processed_reviews'])

  X_t = pad_sequences(list_tokenizer_train, maxlen)
  y = df['label']

  embedding_index = loadGloveModel(glove_dir)
  embedding_matrix = create_emb_matrix(embedding_index, tokenizer, 128)

  network = Network(max_words, maxlen, emb_size, embedding_matrix)
  X_train, X_test, y_train, y_test = train_test_split(X_t, y, test_size=0.2, random_state=123)


  network._model.fit(X_train,
                   y_train,
                   epochs=3,
                   validation_data=(X_test, y_test))


  

  




  '''

  '''


      
  





  










  
  










  ''' 

  parser = NewsParser()
  parser.connect_to_db(path)
  for topic, label in zip(topics, labels):
    parser.get_data(topic, label, 5, True)
  parser.disconnect()
  print('DONE!')
  network._model.fit(X_train,
                     y_train,
                     epochs=3,
                     batch_size=16,
                     validation_data=(X_test, y_test))


  tokenizer = Tokenizer(maxlen)
  tokenizer.fit_on_texts(cleaner.text)
  X = cleaner.to_pad(tokenizer, maxlen)
  y = data['label'].values
  print(embedding_matrix[0])
  print()
  '''



