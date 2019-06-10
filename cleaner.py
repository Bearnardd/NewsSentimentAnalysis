#!/usr/bin/env python3


import unicodedata  
import inflect
from collections import Counter
import re
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk import word_tokenize
from tensorflow.keras.preprocessing.sequence import pad_sequences


class Cleaner:
  def __init__(self, df):
    self.df = df
  
  def create_dataset(self, column):
    self.text = list(self.df[column])
    new_words = []
		


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
  

  def word2idx(self):
    '''
    Takes as input tokenized text and
    return word2idx dict
    '''
    text_all = [' '.join(line) for line in self.text]
    all_reviews = ' '.join(text_all)
    words = all_reviews.split()
    total_words = len(words)
    count_words = Counter(words)
    sorted_words = count_words.most_common(total_words)
    self.word2idx = {w:i+1 for i, (w,c) in enumerate(sorted_words)}


  def encode_reviews(self):
    self.reviews_int = []
    for review in self.text:
      r = [self.word2idx[word] for word in review]
      self.reviews_int.append(r)

  
  def to_pad(self, tokenizer, maxlen):
    seq = tokenizer.texts_to_sequences(self.text)
    pad = pad_sequences(seq, maxlen=maxlen)
    return pad
   
    

          
        
    
        
              

    





    
  

