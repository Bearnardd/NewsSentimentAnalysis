#!/usr/bin/env python3

import tensorflow as tf
from tensorflow.keras.layers import (Dense, LSTM, Embedding, GlobalMaxPool1D,
                         Dropout, Input, Bidirectional, BatchNormalization)
from tensorflow.keras.backend import binary_crossentropy
from tensorflow.keras.models import Model
import warnings
warnings.filterwarnings('ignore')


class Network:
  def __init__(self, max_words, maxlen, embeded_size, embedding_matrix, new=True, path):
    self.max_words = max_words
    self.maxlen = maxlen
    self.embeded_size = embeded_size
    self.embedding_matrix = embedding_matrix
    if new:
        self._model = self.create_model()
    else:
        self._model = load_model(path)


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
    model.compile(loss=self.loss,
                  optimizer='adam',
                  metrics=['acc'])
    return model


  def fit_data(X, y, epochs, bs, validation_split, save=False, path=None):
    self._model.fit(X, y, epochs=epochs, batch_size=bs,
                    validation_split=validation_split)
    if save:
      self._model.save(path)


