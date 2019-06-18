#!/usr/bin/env python3

from flask import Flask, render_template, url_for, request
import pandas as pd
from keras.models import load_model
from keras.preprocessing.text import Tokenizer
from cleaner import Cleaner
from network import Network
from newsparser import NewsParser
import os
import tensorflow as tf
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 
tf.logging.set_verbosity(tf.logging.ERROR)

maxlen = 100
max_words = 20000
emb_size = 50

network = Network(max_words, maxlen, emb_size, None, False, 'data/my_model_3.h5')


app = Flask('Classifier')

global graph
graph = tf.get_default_graph()


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/predict', methods=['POST'])



def predict():
    network.connect_to_db('./data/news.db')
    if request.method == 'POST':
        topic = request.form['topic']
        print(topic)
        with graph.as_default():
            prediction = network.predict_news(topic=topic, page_size=1, database=True)
            print(network.parser.titles[0])
            print(prediction)
   
    return render_template('result.html', prediction=prediction, text=network.parser.titles[0])



if __name__ == '__main__':
    app.run(port=5000, debug=True)
