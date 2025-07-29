from flask import Flask, render_template
import firebase_admin
## from firebase_admin import firestore
from google.cloud import firestore

app = Flask(__name__)
firestore_app = firebase_admin.initialize_app()
db = firestore.Client(database="datadog-demo-db")

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/library")
def library():
    books = db.collection("books").get()
    return render_template('library.html', library_list=books)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
