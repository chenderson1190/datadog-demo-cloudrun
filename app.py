import signal
import sys
from types import FrameType

from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello() -> str:
    return "Hello, World!"


if __name__ == "__main__":
    app.run(host="localhost", port=8080, debug=True)
