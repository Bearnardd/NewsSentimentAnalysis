#!/usr/bin/env python3


import unicodedata  
import inflect
import re
from nltk.corpus import stopwords
'''Clean the data'''
class Cleaner:
  def __init__(self, df):
    self.df = df
  
  def create_dataset(self, column):
    self.text = list(self.df[column])

   
  def remove_non_ascii(self):
    new_words = []
    for word in self.text:
      new_word = unicodedata.normalize('NFKD', word).encode('ascii', 'ignore').decode('utf-8', 'ignore')
      new_words.append(new_word)
    self.text = new_words


  def to_lowercase(self):
    new_words = []
    for word in self.text:
      new_word = word.lower()
      new_words.append(word)
    self.text = new_words


  def remove_punctuation(self):
    new_words = []
    for word in self.text:
      new_word = re.sub(r'[^\w\s]', '', word)
      if new_word != '':
        new_words.append(new_word)
    self.text = new_words


  def remove_number(self):
    p = inflect.engine()
    new_words = []
    for word in self.text:
      if word.isdigit():
        new_word = p.number_to_words(word)
        new_words.append(new_word)
      else:
        new_words.append(new_word)
    self.text = new_words

  
  def remove_stopwords

    
  

