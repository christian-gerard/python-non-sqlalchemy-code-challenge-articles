class Article:
    all = []
    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        type(self).all.append(self)
    
    @property
    def title(self):
        return self._title 
    @title.setter
    def title(self,title):
        if hasattr(self, "title"):
            raise AttributeError('Cannot edit name')
        elif not isinstance(title,str):
            raise ValueError('Must be a string')
        else:
            self._title = title


class Author:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name 
    
    @name.setter
    def name(self, name):
        if hasattr(self, "name"):
            raise AttributeError('Cannot edit name')
        elif not isinstance(name, str):
            raise ValueError('Must be a string')
        elif not len(name) > 0:
            raise ValueError('MUST BE LONGER THAN 0')
        else:
            self._name = name
        

    def articles(self):

        return [article for article in Article.all if article.author.name == self.name ]

    def magazines(self):

        return list({article.magazine for article in Article.all if article.author.name == self.name})

    def add_article(self, magazine, title):
        new_article = Article(self, magazine, title)
        return new_article

    def topic_areas(self):
        topics = list({article.magazine.category for article in Article.all if article.author.name == self.name})
        return topics if topics else None
class Magazine:

    all = []

    def __init__(self, name, category):
        self.name = name
        self.category = category
        type(self).all.append(self)

    @property
    def name(self):
        return self._name 
    
    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise ValueError('Must be a string')
        elif not (len(name) <= 16 and len(name) >= 2):
            raise ValueError('Must be between 2 and 16')
        else:
            self._name = name

    @property
    def category(self):
        return self._category 
    
    @category.setter
    def category(self, category):
        if not isinstance(category, str):
            raise ValueError('Must be a string')
        elif not len(category) > 0:
            raise ValueError('Must be longer than 0')
        else:
            self._category = category

    def articles(self):
        return [article for article in Article.all if article.magazine.name == self.name ]

    def contributors(self):
        return  list({article.author for article in Article.all if article.magazine.name == self.name })

    def article_titles(self):
        
        titles = [article.title for article in Article.all if article.magazine.name == self.name ]
        return titles if titles else None

    def contributing_authors(self):
        authors = [ article.author for article in Article.all if  article.magazine.name == self.name] 
        count = {}

        for author in authors:
            count[author] = authors.count(author)
        
        contributing = list({ key: value for key, value in count.items() if value >= 2})
            
        return contributing if contributing else None
    
    @classmethod
    def top_publisher(cls):

        articles_per_mag = {}
        mags_w_articles = {}

        for mag in Magazine.all:

            if mag not in articles_per_mag:
                articles_per_mag[mag] = 0
            
            for article in Article.all:
                if mag == article.magazine:
                    articles_per_mag[mag] += 1

        for mag in articles_per_mag.items():
            if not mag[1] > 0:
                articles_per_mag[mag[0]] = None

        mags_w_articles = {key: value for key, value in articles_per_mag.items() if value != None}

        if not mags_w_articles:
            return None
        else:
            max_key = max(mags_w_articles.items(), key=lambda x: x[1])
            return max_key[0]


        
        

