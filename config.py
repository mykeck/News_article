import os
from dotenv import load_dotenv
load_dotenv()


class Config:

    API_KEY = os.environ.get("API_KEY")
    SECRET_KEY=os.environ.get("SECRET_KEY")
    NEWS_API_BASE_URL='https://newsapi.org/v2/sources?language=en&category={}&apiKey={}'
    NEWS_ARTICLES_APL_URL='https://newsapi.org/v2/everything?q={}&apiKey={}'
    SOURCE_ARTICLES_URL='https://newsapi.org/v2/everything?sources={}&apiKey={}'


class DevConfig(Config):
    DEBUG = True
    
config_options = {
'development':DevConfig
# 'production':ProdConfig
}