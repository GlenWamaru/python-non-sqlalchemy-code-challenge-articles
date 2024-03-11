class Article:
    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title

class Author:
    def __init__(self, name):
        self.name = name
        self.articles = []

    def add_article(self, magazine, title):
        article = Article(self, magazine, title)
        self.articles.append(article)
        return article

    def articles(self):
        return self.articles

    def magazines(self):
        return list(set(article.magazine for article in self.articles))
    
    def topic_areas(self):
        return list(set(magazine.category for magazine in self.magazines))
    

class Magazine:
    def __init__(self, name, category):
        self.name = name
        self.category = category
        self.articles = []

    def add_article(self, author, title):
        article = Article(author, self, title)
        self.articles.append(article)
        return article
    
    def articles(self):
        return self.articles
    
    def contributors(self):
        authors = [article.author for article in self.articles]
        return list(set(author for author in authors if authors.count(author) > 2))

    def article_titles(self):
        return [article.title for article in self.articles]
    
    def contributing_authors(self):
        return self.contributors()