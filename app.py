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

@app.route('/books/<int:id>', methods=['GET'])
def book(id):
    book = next((b for b in books if b["id"] == id), None)

    if book is None:
        return jsonify({"error": "Book not found"}), 404
    
    return jsonify(book)

@app.route("/books", methods=['POST'])

def create_book():
    data = request.get_json()

    new_book = {
        "id": books[-1]["id"] + 1 if books else 1,
        "title": data["title"],
        "author": data["author"]
    }

    books.append(new_book)
    return jsonify(new_book), 201

@app.route('/books/<int:id>', methods=['PUT'])

def update_book(id):
    data = request.get_json()

    for book in books:
        if book["id"] == id:
            book["title"] = data.get("title", book["title"])
            book["author"] = data.get("author", book["author"])
            return jsonify(book)
    
    return jsonify({"error": "Book not found"}), 404
    
@app.route("/books/<int:id>", methods=['DELETE'])

def delete_book(id):
    global books
    books = [b for b in books if b["id"] != id]

    return jsonify({"message": "Book deleted successfully"})

if __name__ == '__main__':
    print("Starting Flask app...")
    app.run(debug=True)