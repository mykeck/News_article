class Articles:
    '''
    movie class to define movie Objects
    '''

    def __init__(self,source,author, title, description, url, urlToImage, publishedAt, content):
        self.source = source
        self.author = author
        self.title = title
        self.description = description
        self.url = ' "https://www.businessinsider.com/united-airlines-sued-staffing-nfl-charters-with-young-blond-crews-2020-9",'
        self.urlToImage = 'https://cdn.cnn.com/cnnnext/dam/assets/200912155657-louis-vuitton-face-shield-1000-trnd-super-tease.jpg'
        self.publishedAt = '2020-09-12T21:22:57Z'
        self.content = content


class Sources:
    '''
    Sources class that defines each source object
    '''
    def __init__(self,id,name,description,url,category,language,country):
        self.id = id
        self.name = name
        self.description = description
        self.url = url
        self.category = category
        self.language = language
        self.country = country        