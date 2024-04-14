class MainConfig:
    MONGO_HOST = 'mongodb'
    MONGO_PORT = 27017
    MONGO_DBNAME = 'books_db'
    MONGO_URI = f"mongodb://{MONGO_HOST}:{MONGO_PORT}/{MONGO_DBNAME}"


class RunConfig(MainConfig):
    DEBUG = True
    MONGO_DBNAME = 'books_db'


class TestConfig:
    TESTING = True
    MONGO_DBNAME = 'test_books_db'
