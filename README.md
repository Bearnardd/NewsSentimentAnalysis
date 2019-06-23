# NewsSentimentAnalysis
## Description
I realized that most of the newses I read were negative. So I decided to create
app that classifies the newest news from the topic I choose so I do not have to 
read negative ones (of course it is only for fun :3).

### Info!
To get new newses from NewsApi You have to pay money, unfortunately I am a student 
and do not have cash :) so I can not afford it. So without paying You will get
the same news for the same topic all over again.

## The way app operates 
So basically we use News API to pick newses. Then we use neural net to classify
whener it is positive or negative news. For deployment we use flask with the 
simples configuration I can imagine. By default title, description and 

## Usage
Usage is really easy:
1.(Docker)
 - docker build -t <choose image name> 
 - docker run -it -p 5000:5000 <image name>
 @params:
 - -it -> interactive mode
 - -p -> port: in dockerfile we exsposed port 5000

2.(Manual)
 - news.db is already created is data folder so You do not have to create it
 by yourown, but it is possible with ./create_db.py file.
 
 - You just need to run app with ./app.py script and that's all.

 - app.py uses already trained neural net (to be honest there is a huge, huge 
 room for improvment), but If You want to train your own in main.py file there
 is function learn_and_save_model where You can train your own network.

## TODO
 - describe functions, classes etc.


