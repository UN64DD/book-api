from flask import Flask, jsonify, request

app = Flask(__name__)

# Temporary in-memory database
books = [{"id": 1, "title": "Atomic Habits", "author": "James Clear"},
         {"id": 2, "title": "Deep Work", "author": "Cal Newport"}]

@app.route('/')

def home():
    return "Book API is running"