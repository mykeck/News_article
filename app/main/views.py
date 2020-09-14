from flask import render_template,request,redirect,url_for
from .import main
from ..request import get_articles, get_sources,search_articles,articles_source

# Views
@main.route('/')
def index():

    '''
    view root page function that returns the index page and its data
    '''
    #getting articles
    general_news = get_articles('general')
    health = get_articles('category=health')
    technology = get_articles('category= technology')
    title = 'welcome to best Online News'
    return render_template('index.html',title = title,general=general_news, technology=technology, health=health)

@main.route('/articles/<int:id>')
def articles(id): 
    

    return render_template('articles.html', title=title)   