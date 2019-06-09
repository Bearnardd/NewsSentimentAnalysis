#!/usr/bin/env python3

import tensorflow as tf
from tensorflow.keras.layers import (Dense, LSTM, Embedding, GlobalMaxPool1D,
                         Dropout, Input, Bidirectional, BatchNormalization)
from tensorflow.keras.backend import binary_crossentropy
from tensorflow.keras.models import Model


class Network:
  def __init__(self, max_words, maxlen, embeded_size, embedding_matrix):
    self.max_words = max_words
    self.maxlen = maxlen
    self.embeded_size = embeded_size
    self.embeding_matrix = embedding_matrix
    self._model = self.create_model()


  def loss(self, y, y_pred):
    return binary_crossentropy(y, y_pred)


  def create_model(self):
    inputs = Input(shape=self.maxlen,)
    x = Embedding(self.max_words, self.embeded_size,
                  weights=[self.embedding_matrix], trainable=True(intputs)
    x = Bidirectional(LSTM(50, return_sequences=True, dropout=0.1,
                  recurrent_dropout=0.1)(x)
    x = GlobalMaxPool1D()(x)
    x = BatchNormalization(x)
    x = Dense(50, activation='relu')(x)
    x = Dropout(0.1)(x)
    outputs = Dense(2, activation='sigmoid')(x)

    model = Model(inputs=inputs, outputs=outputs)
    model.compile(loss=self.loss()
                  optimizer='nadam',
                  metrics=['acc'])
    return model

