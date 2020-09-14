import urllib.request, json
from .models import models

source = models.source
Article = models.Article

#Getting api key
api_key = None

#getting the movie base url
base_url = None

def configure_request(app):
    global api_key,base_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['NEWS_API_BASE_URL']


def get_articles(filter):
    '''
    Function that gets the json response tou our url request
    '''
    #get_articles('category=bbc-news')
    get_articles_url = base_url.format('top-headlines',api_key,filter)

    with urllib.request.urlopen(get_articles_url) as url:
        get_articles_data = url.read()
        get_articles_response = json.loads(get_articles_data)

        article_results = None

        if get_articles_response['articles']:
            article_results_list = get_articles_response['articles']
            article_results = process_articles(article_results_list)

    return article_results        

