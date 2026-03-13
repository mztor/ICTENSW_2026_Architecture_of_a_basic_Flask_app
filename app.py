# Import dependencies
from flask import Flask


# Create an instance of the Flask class in the app variable
app = Flask(__name__)


# Define the route for the index page at domain root
@app.route("/", methods=["GET"])
def index_page():
    return "Hello World", 200


# Initialize the Flask application
if __name__ == "__main__":
    app.run(debug=True)
