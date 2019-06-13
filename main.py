#!/usr/bin/env python3

'''
  TODO:
   - use parser class to get
     newses and predict 
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
  df = pd.read_csv('imdb_master.csv', encoding='latin-1')
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


def to_pad(df, col, tokenizer, maxlen):
  list_train = df[col].values
  tokenizer.fit_on_texts(list(list_train))
  list_tokenized_train = tokenizer.texts_to_sequences(list_train)
  pad = pad_sequences(list_tokenized_train, maxlen)
  return pad


if __name__ == '__main__':
  cleaner = Cleaner()
  df = get_balanced_dataset()
  tokenizer = Tokenizer(max_words) 
  X_t = to_pad(df['comment_text'].values, tokenizer, maxlen)
  y = df['toxic'].values
  embedding_idx = dict(get_coefs(*o.strip().split()) for o in open(glove_dir, 'r'))
  all_embs = np.stack(embedding_idx.values())
  emb_mean, emb_std = all_embs.mean(), all_embs.std()
  embedding_matrix = create_emb_matrix(embedding_idx, tokenizer, emb_size)
  network = Network(max_words, maxlen, emb_size, embedding_matrix, True, )
  network._model.fit_data(X_t, y, epochs=2, batch_size=128, validation_split=0.1,
                        True, 'my_model_1.h5')
