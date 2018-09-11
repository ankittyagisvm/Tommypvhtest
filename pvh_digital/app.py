"""
Module for PVH Digital Assistant
Creating and Setting up Flask object and
Starting Execution of Application
"""
from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    """home page"""
    return "PVH Tommy Japan Digital Assistant App", 200


if __name__ == "__main__":
    app.run(debug=True)
