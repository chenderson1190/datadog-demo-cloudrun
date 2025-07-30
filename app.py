from flask import Flask, render_template, request
from wtforms import Form, StringField
import google.cloud.logging as logging
import firebase_admin
from google.cloud import firestore
import logging as log

app = Flask(__name__)
firestore_app = firebase_admin.initialize_app()
db = firestore.Client(database="datadog-demo-db")

logging_client = logging.Client()
logging_client.setup_logging()

class Book:
    def __init__(self, book_name, author):
        self.book_name = book_name
        self.author = author

class AddBookForm(Form):
    book_name = StringField("Book Name")
    author = StringField('Author')

@app.route("/")
def index():
    log.info("Index page visited...")
    return render_template('index.html')

@app.route("/library")
def library():
    log.info("Retrieving books from database...")
    books = db.collection("books").get()
    log.info("Books retrieved.")
    return render_template('library.html', library_list=books)

@app.route("/add_book", methods=['GET', 'POST'])
def add_book():
    form = AddBookForm(request.form)
    if request.method == 'POST' and form.validate():
        newBook = {"book_name": str(form.book_name), "author": str(form.author)}
        db.collection("books").add(newBook)
        return redirect(url_for('index'))
    return render_template('add_book.html', form=form)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
