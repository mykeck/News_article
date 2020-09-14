import urllib.request, json
from .models import Article

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

def process_results(article_list):

    article_results = []
    for article_item in article_list:
        source = article_item.get('source')
        author = article_item.get('author') 
        title = article_item.get('title')
        description = article_item.get('description')
        url = article_item.get('url')
        urlToImage = article_item.get('urlToImage')
        publishedAt = article_item.get('publishedAt')
        content = article_item.get('content')

        if content and urlToImage:
            article_object = Article(source,author,title,description,url,urlToImage, publishedAt, content)
            article_results.append(article_object)


