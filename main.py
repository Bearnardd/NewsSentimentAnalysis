#!/usr/bin/env python3


'''
  TODO:
    - update README file
    - Get more data to impove classification, cause atm it 
      is not the best :) 
'''

import tensorflow as tf
from newsparser import NewsParser
from network import Network
from cleaner import Cleaner
from keras.preprocessing.text import Tokenizer
from sklearn.model_selection import train_test_split
from keras.preprocessing.sequence import pad_sequences
from keras.models import load_model
import h5py
import sqlite3
import pandas as pd
import numpy as np
import os
import warnings
warnings.filterwarnings('ignore')
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'


data_dir = os.path.join(os.getcwd(), 'data/train.csv')
dow_path = '/home/bartek/Downloads/'
glove_dir = os.path.join(dow_path, 'glove.6B.50d.txt')
maxlen = 100
max_words = 20000
emb_size = 50
batch_size = 128
epochs = 2


def get_data(path):
  df = pd.read_csv(path, encoding='latin-1')
  df = df[['comment_text', 'toxic']]
  df['comment_text']= df.comment_text.apply(lambda x: cleaner.clean_data(x))
  return df
  

def get_df():
  df = pd.read_csv('./data/imdb_master.csv', encoding='latin-1')
  df = df[df.label=='neg']
  df = df[['review', 'label']]
  df['label'] = df.label.map({'neg':1})
  df = df.rename(columns={'review':'comment_text', 'label':'toxic'})
  df['comment_text'] = df.comment_text.apply(lambda x: cleaner.clean_data(x))
  return df
  

def get_balanced_dataset():
  df_1 = get_data(data_dir)
  df_2 = get_df()
  data = pd.concat([df_1, df_2])
  pos = data[data.toxic==0].sample(len(data[data.toxic==1]))
  neg = data[data.toxic==1]
  df = pd.concat([pos, neg])
  df = df.sample(frac=1)
  df = df.reset_index(drop=True)
  return df


def get_coefs(word,*arr): 
    return word, np.asarray(arr, dtype='float32')


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



def learn_and_save_model(network, path):
  df = get_balanced_dataset()
  X = to_pad(df['comment_text'].values, tokenizer, maxlen)
  y = df['toxic'].values
  embedding_idx = dict(get_coefs(*o.strip().split()) for o in open(glove_dir, 'r'))
  all_embs = np.stack(embedding_idx.values())
  emb_mean, emb_std = all_embs.mean(), all_embs.std()
  embedding_matrix = create_emb_matrix(embedding_idx, tokenizer, emb_size)
  network.fit_data(X, y, epochs=2, batch_size=128, validation_split=0.1, save=True,
      path=path)


if __name__ == '__main__':
  network = Network(max_words, maxlen, emb_size, new=False, path='my_model_2.h5')
  #learn_and_save_model(network, 'my_model_2.h5')
  network.connect_to_db('./data/news.db')
  network.predict_news('Murder', 5, True)



 
  



  
 

  
  

