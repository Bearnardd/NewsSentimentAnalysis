#!/usr/bin/env python3


import unicodedata  
import inflect
import re
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk import word_tokenize
'''Clean the data'''
class Cleaner:
  def __init__(self, df):
    self.df = df
  
  def create_dataset(self, column, tokenize=True):
    self.text = list(self.df[column])
    new_words = []
    if tokenize:
      for line in self.text:
        word = word_tokenize(line)
        new_words.append(word)
        print(new_words)
        break
      self.text = new_words



   
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
      new_words.append(new_word)
 
    self.text = new_words


  def remove_punctuation(self):
    new_words = []
    for word in self.text:
      new_word = re.sub(r'[^\w\s]', '', word)
      if new_word != '':
        new_words.append(new_word)
    self.text = new_words


  def replace_numbers(self):
    p = inflect.engine()
    new_words = []
    for word in self.text:
      if word.isdigit():
        new_word = p.number_to_words(word)
        new_words.append(new_word)
      else:
        new_words.append(word)
    self.text = new_words

  
  def remove_stopwords(self):
    new_words = []
    for word in self.text:
      if word not in stopwords.words('english'):
        new_words.append(word)
    self.text = new_words


  def lemmatize_verbs(self):
    lemmatizer = WordNetLemmatizer()
    lemmas = []
    for word in self.text:
      lemma = lemmatizer.lemmatize(word, pos='v')
      lemmas.append(lemma)
    self.text = lemmas


  def normalize(self):
    new_words = []
    i = 0
    self.remove_non_ascii()
    self.to_lowercase()
    self.remove_punctuation()
    self.replace_numbers()
    self.remove_stopwords()
    self.lemmatize_verbs()
    for text in self.text:
      new_text = word_tokenize(text)
      new_words.append(new_text)
    self.text = new_words



    





    
  

