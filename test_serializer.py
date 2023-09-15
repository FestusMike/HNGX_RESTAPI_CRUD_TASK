from flask import Flask, jsonify
from marshmallow import Schema, fields

app = Flask(__name__)

# Sample data
books = [
    {"id": 1, "title": "Book 1", "author": "Author 1"},
    {"id": 2, "title": "Book 2", "author": "Author 2"},
]

# Define a schema for Book serialization
class BookSchema(Schema):
    id = fields.Int()
    title = fields.Str()
    author = fields.Str()

@app.route('/books', methods=['GET'])
def get_books():
    book_schema = BookSchema(many=True)
    books_json = book_schema.dump(books)
    return jsonify(books_json), 200

if __name__ == '__main__':
    app.run(debug=True)
