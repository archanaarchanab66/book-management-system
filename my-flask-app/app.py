
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

books = [
    {'id': 1, 'name': 'Book 1', 'author': 'Author 1', 'status': 'Available'},
    {'id': 2, 'name': 'Book 2', 'author': 'Author 2', 'status': 'Issued'}
]

@app.route('/books', methods=['GET'])
def get_books():
    return jsonify(books)

@app.route('/books', methods=['POST'])
def add_book():
    new_book = request.json
    new_book['id'] = len(books) + 1
    books.append(new_book)
    return jsonify(new_book)

@app.route('/books/<int:id>', methods=['PUT'])
def update_book(id):
    updated_book = request.json
    for book in books:
        if book['id'] == id:
            book.update(updated_book)
            return jsonify(book)
    return jsonify({'message': 'Book not found'}), 404

@app.route('/books/<int:id>', methods=['DELETE'])
def delete_book(id):
    global books
    books = [book for book in books if book['id'] != id]
    return jsonify({'message': 'Book deleted'})

if __name__ == '__main__':
    app.run(debug=True)
