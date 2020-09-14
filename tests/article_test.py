import unittest
from ..app import models
Article = modules.Article


class ArticleTest(unittest.TestCase):
    '''
    Test class to test the behavior of the Article class
    '''

    def setUp(self):
        '''
        set up method that will run before every test
        '''
        self.new_article = Article('','','','','','','','')

    def test_instance(self): 
        self.assertTrue(isinstance(self.new_article,Article))   

    