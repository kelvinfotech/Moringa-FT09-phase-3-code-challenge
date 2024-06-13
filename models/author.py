# models/author.py


class Author:
    def __init__(self, id, name):
        self._id = id
        self._name = name
        
        # Simulate saving to database by printing a message
        print(f"Author '{self._name}' is initialized with id {self._id} and saved to the database.")

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
    
    def articles(self):
        from models.article import Article
        # Simulating retrieval of articles from database
        # Here, assuming Article is imported correctly from models.article
        return [
            Article(1, "Test Title 1", "Test Content 1", self._id, 1),
            Article(2, "Test Title 2", "Test Content 2", self._id, 2)
        ]  # Replace with actual retrieval logic using SQL JOINs
    
    def magazines(self):
        from models.magazine import Magazine
        # Simulating retrieval of magazines from database
        # Here, assuming Magazine is imported correctly from models.magazine
        return [
            Magazine(1, "Tech Weekly", "Technology"),
            Magazine(2, "Science Monthly", "Science")
        ]  # Replace with actual retrieval logic using SQL JOINs
    
    def __repr__(self):
        return f'<Author {self._name}>'
