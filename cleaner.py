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
  def __init__(self, text):
    self.lemmatizer = WordNetLemmatizer()
    self.stop_words = set(stopwords.words('english'))
    
  def clean_data(self, text):
    text = re.sub('[^\w\s]', '', text, re.UNICODE)
    text = text.lower()
    text = [self.lemmatizer.lemmatize(token) for token in text.split(' ')]
    text = [self.lemmatizer.lemmatize(token, 'v') for token in text]
    text = [word for word in text if not word in self.stop_words]
    text = unicodedata.normalize('NFKD', text).encode('ascii', 'ignore').decode('utf-8', 'ignore')
    text = ' '.join(text)
    return text

     

   
    

          
        
    
        
              

    





    
  

