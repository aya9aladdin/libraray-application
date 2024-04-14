import json

from flask import Flask, jsonify
from flask_restful import Resource, Api, reqparse
from flask_pymongo import PyMongo
from bson import json_util, ObjectId
from flask_cors import CORS

def get_app_with_config(config):
    app = Flask(__name__)
    app.config.from_object(config)

    mongo = PyMongo(app)

    CORS(app, resources={r"/*":{'origins':"*"}})

    COLLECTION = "books"

    api = Api(app)

    parser = reqparse.RequestParser()
    parser.add_argument('title', type=str, required=True, help='title is required')
    parser.add_argument('ISBN', type=int, required=True, help='ISBN is required')
    parser.add_argument('genre', type=str, required=True, help='genre is required')
    parser.add_argument('author', type=str, required=True, help='author is required')
    parser.add_argument('pub_year', type=int, required=True, help='pub_year is required')


    class BooksRetrieval(Resource):
        def get(self):
            data = mongo.db[COLLECTION].find()

            books = json.loads(json_util.dumps(data))

            for book in books:
                book['_id'] = book['_id']['$oid']

            return books, 200

        def post(self):
            args = parser.parse_args()
            if mongo.db[COLLECTION].find_one({"ISBN": args.ISBN}):
                response = {
                    "message": "Book with this ISBN already exists",
                    "status_code": 409
                }
            else:
                mongo.db[COLLECTION].insert_one(args)
                response = {
                    "message": "Book added successfully"
                }
            return response, 200

        
    class BookModify(Resource):
        def get(self, book_id):
            try:
                obj_id = ObjectId(book_id)
            except Exception as e:
                return {"error": "Invalid ObjectId"}, 400

            book = mongo.db[COLLECTION].find_one({"_id": obj_id})
            if (not book):
                return {"error": "ID not found"}, 404
                
            book = json.loads(json_util.dumps(book))
            book["_id"] = book["_id"]["$oid"]
            return book, 200
        
        def put(self, book_id):
            args = parser.parse_args()
            data = mongo.db[COLLECTION].update_one(
            {"_id": ObjectId(book_id)},
            {"$set": args}
        )
            
            if data.matched_count == 0:
                return {"error": "Book not found"}, 404

            return {"message": "Book updated successfully"}, 200

        def delete(self, book_id):
            
            try:
                obj_id = ObjectId(book_id)
            except Exception as e:
                return {"message": "Invalid ObjectId"}, 400
            
            book = mongo.db[COLLECTION].find_one({"_id": obj_id})

            if (not book):
                return {"message": f"book with this ID: {book_id} is not found"}, 404
                
            book = json.loads(json_util.dumps(book))
            book["_id"] = book["_id"]['$oid']
            mongo.db[COLLECTION].delete_one({"_id": obj_id})
            return book, 200

    api.add_resource(BooksRetrieval, '/books/')
    api.add_resource(BookModify, '/books/<string:book_id>')

    return app, mongo
