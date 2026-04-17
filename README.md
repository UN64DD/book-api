

# 📚 Book API

A simple RESTful Book Management API built with Flask.
This project demonstrates core backend development concepts such as routing, CRUD operations, and JSON-based request handling.

---

## 🚀 Features

* Create a new book
* Retrieve all books
* Retrieve a single book by ID
* Update book details
* Delete a book
* Simple in-memory data storage (no database required)

---

## 🛠️ Tech Stack

* Python 3
* Flask

---

## 📁 Project Structure

```
book-api/
│── app.py
│── requirements.txt
│── README.md
```

---

## ⚙️ Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/your-username/book-api.git
cd book-api
```

---

### 2. Create virtual environment

```bash
python -m venv venv
```

Activate it:

**Windows**

```bash
venv\Scripts\activate
```

**Mac/Linux**

```bash
source venv/bin/activate
```

---

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Run the application

```bash
python app.py
```

Server will run at:

```
http://127.0.0.1:5000/
```

---

## 📌 API Endpoints

### 🏠 Home

```
GET /
```

Response:

```
Book API is running!
```

---

### 📚 Get all books

```
GET /books
```

---

### 🔍 Get book by ID

```
GET /books/<id>
```

Example:

```
GET /books/1
```

---

### ➕ Create a book

```
POST /books
```

Request Body:

```json
{
  "title": "Clean Code",
  "author": "Robert C. Martin"
}
```

---

### ✏️ Update a book

```
PUT /books/<id>
```

Request Body:

```json
{
  "title": "Updated Title",
  "author": "Updated Author"
}
```

---

### ❌ Delete a book

```
DELETE /books/<id>
```

---

## 🧠 Learning Outcomes

This project helps you understand:

* REST API design principles
* Flask routing system
* Handling HTTP methods (GET, POST, PUT, DELETE)
* Working with JSON data
* Basic backend architecture

---

## 🚀 Future Improvements

* Add database support (SQLite / PostgreSQL)
* Add user authentication (JWT)
* Add input validation
* Deploy using Render / Railway / Vercel
* Add Swagger API documentation

---

## 👨‍💻 Author

Built as part of a backend learning journey.

---
