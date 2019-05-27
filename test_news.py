#!/usr/bin/env python3

import requests

url = ('https://newsapi.org/v2/top-headlines?'
       'country=us&'
       'apiKey=0fce127066fb4adda75f524c202905eb')
response = requests.get(url)



def get_titles(num):
       url = ('https://newsapi.org/v2/top-headlines?'
             'country=us&'
             'apiKey=Apikey'
       response = requests.get(url)
       for val in range(num):
         title = response.json()['articles'][val]['title']
         content = response.json()['articles'][val]['content']
         description = response.json()['articles'][val]['description']
         print(f'Title number {val}: {title}', end='\n')
         print('')
         print(f'Content number {val}: {content}', end='\n')
         print('')
         print(f'Description number {val}: {description}', end='\n')
         print('')


if __name__ == '__main__':
  get_titles(1)