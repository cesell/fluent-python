from flask import Flask, jsonify, request, Response
import json

app = Flask(__name__)

books = [
    {
        'name': 'Green Eggs and Ham',
        'price': 7.99,
        'isbn': 987908768
    },
    {
        'name': 'The Cat In The Hat',
        'price': 6.99,
        'isbn': 98097789
    }
]

def valid_book(book):
    fields = ['name','price','isbn']
    for field in fields:
        if field not in book:
            return False
    return True

@app.route('/')
def hello_world():
    return '<h1>Books</h1>'

@app.route('/books')
def get_books():
    return jsonify({'books' : books})

@app.route('/books', methods=["POST"])
def add_book():
    request_data = request.get_json() #returns a dictionary
    if valid_book(request_data):
        new_book = {
            "name": request_data['name'],
            "price": request_data['price'],
            "isbn": request_data['isbn']
        }
        books.insert(0, new_book)

        response = Response("", 201, mimetype='application/json')
        response.headers['Location'] = "/books/" + str(new_book['isbn'])
        return response
    else:
        invalidBookErrorMsg = {
            "error" : "Invalid book object passed in request",
            "helpString" : "Use these fields {name, price, isbn}"
        }
        return Response(json.dumps(invalidBookErrorMsg), status=400, 
                        mimetype='application/json')
                            


@app.route('/books/<int:isbn>')
def get_book_by_isbn(isbn):
    return_value = {}
    for book in books:
        if book['isbn'] == isbn:
            return_value = {
                'name':book['name'],
                'prince':book['price']
            }
    return jsonify(return_value)


@app.route('/books/<int:isbn>', methods=['PUT'])
def replace_book(isbn):
    request_data = request.get_json()
    new_book = {
            "name": request_data['name'],
            "price": request_data['price'],
            "isbn": isbn
    }
    for i, book in enumerate(books):
        if book['isbn'] == isbn:
            books[i] = new_book
            return Response("", status=204)
    return Response("", status=400)        

if __name__ == '__main__':

    app.run(port=5000, debug=True)

