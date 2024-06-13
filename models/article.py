# models/article.py

class Article:
    def __init__(self, id, title, content, author_id, magazine_id):
        self._id = id
        self._title = title
        self._content = content
        self._author_id = author_id
        self._magazine_id = magazine_id
        
        # Simulate saving to database by printing a message
        print(f"Article '{self._title}' is initialized and saved to the database.")

    @property
    def id(self):
        return self._id

    @property
    def title(self):
        return self._title

    @staticmethod
    def validate_title(title):
        if not isinstance(title, str):
            raise ValueError("Title must be a string.")
        if len(title) < 5 or len(title) > 50:
            raise ValueError("Title must be between 5 and 50 characters long.")
    
    @title.setter
    def title(self, new_title):
        raise AttributeError("Cannot change the title of the article after instantiation.")
    
    @property
    def author(self):
        from models.author import Author
        # Simulating retrieval of author from database
        # Here, assuming Author is imported correctly from models.author
        return Author(self._author_id, "John Doe")  # Replace with actual retrieval logic
    
    @property
    def magazine(self):
        from models.magazine import Magazine
        # Simulating retrieval of magazine from database
        # Here, assuming Magazine is imported correctly from models.magazine
        return Magazine(self._magazine_id, "Tech Weekly", "Technology")  # Replace with actual retrieval logic
    
    def __repr__(self):
        return f'<Article {self._title}>'
