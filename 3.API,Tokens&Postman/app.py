from flask import Flask, jsonify, request

app = Flask(__name__)

# List of Books
books = [
    {"id":1,"title":"Book 1","author":"Author 1"},
    {"id":2,"title":"Book 2","author":"Author 2"},
    {"id":3,"title":"Book 3","author":"Author 3"},
]

# Home page
@app.route("/",methods=['GET'])
def home():
    return 'HOME PAGE'

# List all books
@app.route("/books",methods=['GET'])
def get_books():
    return jsonify(books)

#  Get a book
@app.route("/books/<int:id>",methods=['GET'])
def get_book(id):
    for book in books:
            if book['id'] == id:
                return jsonify(book)
    return jsonify({"Error":f"No book found with book id = {id}"})

# Add a book
@app.route("/books/<int:id>",methods=['GET','POST'])
def add_book(id):
    newbook = {
         "id":request.json['id'],
         "title":request.json['title'],
         "author":request.json['author']
    }
    books.append(newbook)
    return jsonify({'New Message':'New Book has been added successfully.'})

# Update a book
@app.route("/books/update/<int:id>",methods=['PUT'])
def update_book(id):
    for book in books:
        if book['id'] == id:
            book['id'] = request.json['id']
            book['title'] = request.json['title']
            book['author'] = request.json['author']
            return jsonify({'New Message':'Book has been updated successfully.'})
    
    return jsonify({"Error":f"No book found with book id = {id}"})

# Delete a book
@app.route("/books/<int:id>",methods=['DELETE'])
def delete_book(id):
    for book in books:
        if book['id'] == id:
            books.remove(book)
            return jsonify({'New Message':'Book has been deleted successfully.'})
    
    return jsonify({"Error":f"No book found with book id = {id}"})

    


if __name__ == "__main__":
    app.run(debug=True)