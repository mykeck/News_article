from flask import render_template
from .import main

@main.app_errorhandler(404)
def four_0w_four(error):
    '''
    Function to render the 404 page
    '''
    return render_template('fourowfour.html'),404