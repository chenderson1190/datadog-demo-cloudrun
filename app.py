from flask import Flask, render_template
import logging
import firebase_admin
from google.cloud import firestore
import ddtrace

app = Flask(__name__)
firestore_app = firebase_admin.initialize_app()
db = firestore.Client(database="datadog-demo-db")

logger = logging.getLogger('library_logger')
logging.basicConfig(filename="/shared-volume/logs/library.log")
logger.setLevel(logging.INFO)

@app.route("/")
def index():
    logger.info("Index page visited...")
    return render_template('index.html')

@app.route("/library")
def library():
    logger.info("Retrieving books from database...")
    books = db.collection("books").get()
    logger.info("Books retrieved.")
    return render_template('library.html', library_list=books)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
