# library-management-system

This is a simple full-stack project for a library management system

## Technologies
- Flask restful: for the back-end API
- Vue3 : for front-end 
- MongoDB: for database

## API endpoints
### Adding new book endpoint
POST http://127.0.0.1:5000/books/
{
  "author": srt,
  "ISBN": int,
  "genre": str,
  "title": "str,
  "pub_year": int,
}

### Updadintng existing book
PUT http://127.0.0.1:5000/books/id
{
  "author": srt,
  "ISBN": int,
  "genre": str,
  "title": "str,
  "pub_year": int,
}

### Getting book by id
GET http://127.0.0.1:5000/books/id

### Getting all books
GET http://127.0.0.1:5000/books/

### Delete a book by id
DELETE http://127.0.0.1:5000/books/id


## Vuetify UI
I used some UI components from Vuetify library as the buttons, data table, and cards

## Things to improve
- add tests for the API
- schema validation for the DB
- add alert messages after adding/deleting/updating a book

## running the backend
- you must have MongoDB installed locally on your machine and the server is running
- install requirement.txt
- run ``python backend/main.py``

## running frontend
- ensure that you have npm and vue installed on your machine
- change directory to the project directory:  ``cd frontend/vue_fronend``
-  npm run serve 
- add more error-handling logic in both back and front end

## video dem
https://youtu.be/-3xHnlKLPlc
![alt text](image.png)
