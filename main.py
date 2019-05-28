#!/usr/bin/env python3

from newsparser import NewsParser


'''
TODO:
 - add database and fill news
 - build neural network
 - clean code
'''



if __name__ == '__main__':
  parser = NewsParser()
  parser.get_data('bitcoin', 12)
  titles = parser._titles
  print(len(titles))


