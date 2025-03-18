from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import pymysql

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456@localhost/book_db'
db = SQLAlchemy(app)

# Създаване на базата данни ако не съществува
connection = pymysql.connect(host='localhost', user='root', password='123456')
cursor = connection.cursor()
cursor.execute("CREATE DATABASE IF NOT EXISTS book_db;")
cursor.close()
connection.close()

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(100), nullable=False)

with app.app_context():
    db.create_all()

@app.route('/books', methods=['POST'])
def add_book():
    data = request.json
    new_book = Book(title=data['title'], author=data['author'])
    db.session.add(new_book)
    db.session.commit()
    return jsonify({"message": "Book added"}), 201

@app.route('/books', methods=['GET'])
def get_books():
    books = Book.query.all()
    return jsonify([{ "id": b.id, "title": b.title, "author": b.author } for b in books])

@app.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book = Book.query.get_or_404(book_id)
    return jsonify({"id": book.id, "title": book.title, "author": book.author})

@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    book = Book.query.get(book_id)
    if book:
        db.session.delete(book)
        db.session.commit()
        return jsonify({"message": "Book deleted"}), 200
    return jsonify({"error": "Book not found"}), 404


if __name__ == '__main__':
    app.run(debug=True)