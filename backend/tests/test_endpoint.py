import pytest
import sys
import random

sys.path.append('../')  

from app import get_app_with_config
from config import TestConfig

@pytest.fixture
def client():
    app, mongo = get_app_with_config(TestConfig)
    return app.test_client(TestConfig)


def test_get_books(client):
    response = client.get('/books/')
    assert response.status_code == 200

def test_post_book(client):
    book_data = {
        'title': 'Test Book',
        'ISBN': random.randint(9999, 99999999) ,
        'genre': 'Test Genre',
        'author': 'Test Author',
        'pub_year': 2024
    }

    response = client.post('/books/', json=book_data)

    assert response.status_code == 200

    assert response.json['message'] == "Book added successfully"

def test_post_book_with_missing_data(client):
    book_data = {
        'ISBN': '12345637890',
        'genre': 'Test Genre',
        'author': 'Test Author',
        'pub_year': 2024
    }

    response = client.post('/books/', json=book_data)

    assert response.status_code == 400

    assert response.json['message']["title"] == 'title is required'

def test_get_book_with_id(client):

    book = client.get('/books/').json[0]
    response = client.get(f"/books/{book['_id']}")

    assert response.status_code == 200

    assert response.json['title'] == book['title']

def test_get_book_with_invalid_id(client):

    response = client.get("/books/123")

    assert response.status_code == 400
    assert response.json["error"] == 'Invalid ObjectId'

def test_get_book_with_wrong_id(client):
    id = '1'*24
    response = client.get(f"/books/{id}")

    assert response.status_code == 404
    assert response.json["error"] == 'ID not found'


def test_udpate_book(client):

    book = client.get('/books/').json[0]
    id = book["_id"]
    book["pub_year"] = 11111111

    response = client.put(f"/books/{book['_id']}", json=book)

    assert response.status_code == 200

    assert client.get(f"/books/{id}").json["pub_year"] == 11111111
