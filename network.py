#!/usr/bin/env python3


from keras.layers import (Dense, LSTM, Embedding, GlobalMaxPool1D,
                         Dropout, Input, Bidirectional, BatchNormalization)
from keras.models import Model, load_model
from keras.preprocessing.text import Tokenizer
import warnings
from cleaner import Cleaner
from newsparser import NewsParser
import sqlite3

warnings.filterwarnings('ignore')


class Network:
  def __init__(self, max_words, maxlen, embeded_size, embedding_matrix=None, 
          new=True, path=None):
    self.max_words = max_words
    self.maxlen = maxlen
    self.parser = NewsParser()
    self.cleaner = Cleaner()
    self.tokenizer = Tokenizer(self.max_words)
    self.embeded_size = embeded_size
    self.embedding_matrix = embedding_matrix
    if new:
        self._model = self.create_model()
    else:
        self._model = load_model(path)


  def connect_to_db(self, path):
    self.conn = sqlite3.connect(path)
    self.c = self.conn.cursor()


  def create_model(self):
    inputs = Input(shape=(self.maxlen,))
    x = Embedding(self.max_words, self.embeded_size,
                  weights=[self.embedding_matrix], trainable=False)(inputs)
    x = Bidirectional(LSTM(32, return_sequences=True, dropout=0.1,
                  recurrent_dropout=0.1))(x)
    x = GlobalMaxPool1D()(x)
    x = BatchNormalization()(x)
    x = Dense(20, activation='relu')(x)
    x = Dropout(0.1)(x)
    outputs = Dense(1, activation='sigmoid')(x)

    model = Model(inputs=inputs, outputs=outputs)
    model.compile(loss='binary_crossentropy',
                  optimizer='adam',
                  metrics=['acc'])
    return model


  def fit_data(self, X, y, epochs, batch_size, validation_split, save=False, path=None):
    self._model.fit(X, y, epochs=epochs, batch_size=batch_size,
                    validation_split=validation_split)
    if save:
      if path==None:
        path = input('Path for weights:\n')
      self._model.save(path)
  

  def predict_news(self, topic, page_size, database=True):
    self.parser.get_data(topic=topic, page_size=page_size)
    for page in range(page_size):
        data = self.cleaner.clean_data(self.parser.titles[page])
        pad = self.cleaner.to_pad(data, self.tokenizer, self.maxlen)
        ans = self._model.predict(pad)
        if ans <= 0.5:
          label = 0
        else:
          label = 1 
        
        if database:
          self.c.execute('INSERT INTO news VALUES(?, ?, ?, ?)', (self.parser.titles[page],          self.parser.desc[page], self.parser.content[page], label))
          self.conn.commit()  

    return label


    

