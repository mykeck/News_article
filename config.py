import os
class Config:
    '''
    General configuration parent class
    '''
    NEWS_API_BASE_URL ='http://newsapi.org/v2/{}?apiKey={}&{}'
    NEWS_API_KEY = os.environ.get('NEWS_API_KEY')

class ProdConfig(Config):
    pass

class DevConfig(Config):

    DEBUG = True

Config_options = {
 'development':DevConfig,
 'production':ProdConfig   
}    