import urllib.request, json
from .models import Articles,Sources
import os
# import request

# source = models.source
# Article = models.Article

# #Getting api key
# api_key = None

# #getting the movie base url
# base_url = None

# art_url = None

# def configure_request(app):
#     global api_key,base_url
#     api_key = app.config['NEWS_API_KEY']
#     base_url = app.config['NEWS_API_BASE_URL']


# def get_articles(filter):
#     '''
#     Function that gets the json response tou our url request
#     '''
#     #get_articles('category=bbc-news')
#     get_articles_url = base_url.format('top-headlines',api_key,filter)

#     with urllib.request.urlopen(get_articles_url) as url:
#         get_articles_data = url.read()
#         get_articles_response = json.loads(get_articles_data)

#         article_results = None

#         if get_articles_response['articles']:
#             article_results_list = get_articles_response['articles']
#             article_results = process_articles(article_results_list)

#     return article_results 

# def process_articles(article_list):

#     article_results = []
#     for article_item in article_list:
#         source = article_item.get('source')
#         author = article_item.get('author') 
#         title = article_item.get('title')
#         description = article_item.get('description')
#         url = article_item.get('url')
#         urlToImage = article_item.get('urlToImage')
#         publishedAt = article_item.get('publishedAt')
#         content = article_item.get('content')

#         if content and urlToImage:
#             article_object = Article(source,author,title,description,url,urlToImage, publishedAt, content)
#             article_results.append(article_object)

#     return article_results


# def get_sources():
#     get_sources_url = base_url.format('sources', api_key) 

#     with urllib.request.urlopen(get_sources_url) as url:
#         sources_data = url.read()
#         sources_response = json.loads(sources_data)

#         sources_object = None

#         sources_response_data = sources_response['sources']
#         if sources_response_data:
#             sources_object = process_sources(sources_response_data) 

#     return sources_object


# def process_sources(source_list):

#     source_results = []
#     for source_item in source_list:
#         id = source_item.get('id')
#         name = source_item.get('name')
#         description = source_item.get('description')
#         url = source_item.get('url')
#         category = source_item.get('category')
#         language = source_item.get('language')
#         country = source_item.get('country')

#         sources_object = Source(id, name, description, url, category, language, country)
#         source_results.append(sources_object)

#     return source_results    
api_key = None
s_url = None
art_url = None
secret_key=None
def configure_request(app):
    global api_key,s_url,art_url,secret_key
    api_key = app.config['API_KEY']
    secret_key = app.config['SECRET_KEY']
    articles_url = app.config['SOURCE_ARTICLES_URL']
    s_url = app.config['NEWS_API_BASE_URL']
    art_url = app.config['NEWS_ARTICLES_APL_URL']
def get_sources(category):
    """
    function that gets response from the api call
    """
    sources_url = s_url.format(category,api_key)
    with urllib.request.urlopen(sources_url) as url:
        sources_data = url.read()
        response = json.loads(sources_data)
        sources_outcome = None
        if response['sources']:
            sources_outcome_items = response['sources']
            sources_outcome = process_new_sources(sources_outcome_items)
    return sources_outcome
def process_new_sources(sources_list):
    sources_outcome = []
    for one_source in sources_list:
        id = one_source.get("id")
        name = one_source.get("name")
        description = one_source.get("description")
        url = one_source.get("url")
        category = one_source.get("category")
        language = one_source.get("language")
        country = one_source.get("country")
        new_source = Sources(id,name,description,url,category,language,country)
        sources_outcome.append(new_source)
    return sources_outcome
def get_articles(article):
    articles_url = art_url.format(article,api_key)
    # print(art_url)
    with urllib.request.urlopen(articles_url) as url:
        articles_data = url.read()
        articles_response = json.loads(articles_data)
        articles_outcome = None
        if articles_response['articles']:
            articles_outcome_items = articles_response['articles']
            articles_outcome = process_new_articles(articles_outcome_items)
    return articles_outcome
def process_new_articles(articles_list):
    articles_outcome = []
    for one_article in articles_list:
        source = one_article.get("source")
        author = one_article.get("author")
        description = one_article.get("description")
        title = one_article.get("title")
        url = one_article.get("url")
        urlToImage = one_article.get("urlToImage")
        publishedAt = one_article.get("publishedAt")
        new_article = Articles(source, author, title, description, url, urlToImage, publishedAt)
        articles_outcome.append(new_article)
    return articles_outcome
def articles_source(source):
    sources_a_url = 'https://newsapi.org/v2/sources?apiKey={}'.format(source,api_key)
    with urllib.request.urlopen(sources_a_url) as url:
        art_data = url.read()
        response = json.loads(art_data)
        source_articles = None
        if response['articles']:
            source_articles_list = response['articles']
            source_articles = process_articles_source(source_articles_list)
    return source_articles
def process_articles_source(article_list):
    source_articles = []
    for art in article_list:
        source = art.get("source")
        author = art.get('author')
        title = art.get('title')
        description = art.get('description')
        url = art.get('url')
        urlToImage = art.get('urlToImage')
        publishedAt = art.get('publishedAt')
        article_object = Articles(source,author,title,description,url,urlToImage,publishedAt)
        source_articles.append(article_object)
    return source_articles
def search_articles(article_name):
    search_url = art_url.format(article_name,api_key)
    with urllib.request.urlopen(search_url) as url:
        search_data = url.read()
        search_response = json.loads(search_data)
        search_results = None
        if search_response['articles']:
            all_search_results = search_response['articles']
            search_outcome = process_search(all_search_results)
    return search_outcome

                         


