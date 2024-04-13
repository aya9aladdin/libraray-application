import pytest
import sys
import random

sys.path.append('../')  

from main import app
from pymongo import MongoClient
from config import TestingConfig

DATABASE = "test_books_db"
COLLECTION = "books"

@pytest.fixture
def test_client():
    app.config.from_object(TestingConfig)
    with app.test_client() as test_client:
        yield test_client


def test_get_books(test_client):
    response = test_client.get('/books/')
    assert response.status_code == 200

def test_post_book(test_client):
    book_data = {
        'title': 'Test Book',
        'ISBN': random.randint(9999, 99999999) ,
        'genre': 'Test Genre',
        'author': 'Test Author',
        'pub_year': 2024
    }

    response = test_client.post('/books/', json=book_data)

    assert response.status_code == 200

    assert response.json['message'] == "Book added successfully"

def test_post_book_with_missing_data(test_client):
    book_data = {
        'ISBN': '12345637890',
        'genre': 'Test Genre',
        'author': 'Test Author',
        'pub_year': 2024
    }

    response = test_client.post('/books/', json=book_data)

    assert response.status_code == 400

    assert response.json['message']["title"] == 'title is required'

def test_get_book_with_id(test_client):

    book = test_client.get('/books/').json[0]
    response = test_client.get(f"/books/{book['_id']}")

    assert response.status_code == 200

    assert response.json['title'] == book['title']

def test_get_book_with_invalid_id(test_client):

    response = test_client.get("/books/123")

    assert response.status_code == 400
    assert response.json["error"] == 'Invalid ObjectId'

def test_get_book_with_wrong_id(test_client):
    id = '1'*24
    response = test_client.get(f"/books/{id}")

    assert response.status_code == 404
    assert response.json["error"] == 'ID not found'


def test_udpate_book(test_client):

    book = test_client.get('/books/').json[0]
    id = book["_id"]
    book["pub_year"] = 11111111

    response = test_client.put(f"/books/{book['_id']}", json=book)

    assert response.status_code == 200

    assert test_client.get(f"/books/{id}").json["pub_year"] == 11111111
