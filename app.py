from flask import Flask, jsonify, request

app = Flask(__name__)

# Temporary in-memory database
books = [{"id": 1, "title": "Atomic Habits", "author": "James Clear"},
         {"id": 2, "title": "Deep Work", "author": "Cal Newport"}]

@app.route('/')

def home():
    return "Book API is running"

@app.route('/books', methods=['GET'])

def get_books():
    return jsonify(books)

@app.route('/books/<int: id>', methods=['GET'])
def book(id):
    book = next((b for b in books if b["id"]), None)

    if book is None:
        return jsonify({"error": "Book not found"}), 404
    
    return jsonify(book)