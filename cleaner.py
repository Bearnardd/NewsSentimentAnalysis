#!/usr/bin/env python3


import unicodedata  
import re
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk import word_tokenize
from keras.preprocessing.sequence import pad_sequences
from keras.preprocessing.text import Tokenizer


class Cleaner:
  def __init__(self):
    self.lemmatizer = WordNetLemmatizer()
    self.stop_words = set(stopwords.words('english'))

    

  def clean_data(self, text):
    text = re.sub('[^\n\w\s]', '', text, re.UNICODE)
    text = text.lower()
    text = [self.lemmatizer.lemmatize(token) for token in text.split(' ')]
    text = [self.lemmatizer.lemmatize(token, 'v') for token in text]
    text = [word for word in text if not word in self.stop_words]
    text = ' '.join(text)
    text = unicodedata.normalize('NFKD', text).encode('ascii', 'ignore').decode('utf-8', 'ignore')
    return text

  
  def to_pad(self, data, tokenizer, maxlen):
    data = [data]
    tokenizer.fit_on_texts(data)
    list_tokenized = tokenizer.texts_to_sequences(data)
    pad = pad_sequences(list_tokenized, maxlen)
    return pad
     

   
    

          
        
    
        
              

    





    
  

