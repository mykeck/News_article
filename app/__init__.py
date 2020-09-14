from flask import Flask
from config import Config_options


def create_app(config_name):
    #Initializing application
    app = Flask(__name__)
    
    #setting up configuration
    app.config.from_object(Config_options[config_name])


# from .main import views



