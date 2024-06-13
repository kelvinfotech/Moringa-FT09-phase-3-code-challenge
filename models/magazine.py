# models/magazine.py

from models.article import Article
from models.author import Author

class Magazine:
    def __init__(self, id, name, category):
        self._id = id
        self._name = name
        self._category = category
        self._articles = []

        # Simulate saving to database by printing a message
        print(f"Magazine '{self._name}' ({self._category}) is initialized and saved to the database.")

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name
    
    @staticmethod
    def validate_id(id):
        if not isinstance(id, int):
            raise ValueError("ID must be of type int.")
    
    def article_titles(self):
        # Simulating retrieval of article titles from database
        # Here, assuming Article is imported correctly from models.article
        return [article.title for article in self._articles]
    
    def contributing_authors(self):
        # Simulating retrieval of contributing authors from database
        # Here, assuming Author is imported correctly from models.author
        author_counts = {}
        
        # Count articles per author
        for article in self._articles:
            author_id = article.author_id
            if author_id in author_counts:
                author_counts[author_id] += 1
            else:
                author_counts[author_id] = 1
        
        # Filter authors who have more than 2 articles
        contributing_authors = []
        for author_id, count in author_counts.items():
            if count > 2:
                contributing_authors.append(Author(author_id, f"Author {author_id}"))  # Replace with actual retrieval logic
        
        if len(contributing_authors) == 0:
            return None
        else:
            return contributing_authors
    
    def add_article(self, article):
        self._articles.append(article)
    
    @property
    def category(self):
        return self._category
    
    def __repr__(self):
        return f'<Magazine {self._name}>'
