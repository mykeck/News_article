import os
# class Config:
#     '''
#     General configuration parent class
#     '''
#     NEWS_API_BASE_URL ='http://newsapi.org/v2/sources?apiKey={}'
#     NEWS_API_KEY = os.environ.get('NEWS_API_KEY')

# class ProdConfig(Config):
#     pass

# class DevConfig(Config):

#     DEBUG = True

# Config_options = {
#  'development':DevConfig,
#  'production':ProdConfig   
# }    


class Config:
    API_KEY=os.environ.get("API_KEY")
    SECRET_KEY=os.environ.get("SECRET_KEY")
    NEWS_API_BASE_URL='https://newsapi.org/v2/sources?country=us&category={}&apiKey={}'
    NEWS_ARTICLES_APL_URL='https://newsapi.org/v2/everything?q={}&apiKey={}'
    SOURCE_ARTICLES_URL='https://newsapi.org/v2/everything?sources={}&apiKey={}'


class DevConfig(Config):
    DEBUG = True
config_options = {
'development':DevConfig
# 'production':ProdConfig
}