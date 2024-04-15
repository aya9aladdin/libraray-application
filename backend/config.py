class RunConfig():
    MONGO_HOST = 'localhost'
    MONGO_PORT = 27017
    DEBUG = True
    MONGO_DBNAME = 'books_db'
    MONGO_URI = f"mongodb://{MONGO_HOST}:{MONGO_PORT}/{MONGO_DBNAME}"


class TestConfig():
    MONGO_HOST = 'localhost'
    MONGO_PORT = 27017
    TESTING = True
    MONGO_DBNAME = 'test_books_db'
    MONGO_URI = f"mongodb://{MONGO_HOST}:{MONGO_PORT}/{MONGO_DBNAME}"
