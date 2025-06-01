# This is a simple Flask application that returns "Hello, World!" when accessed at the root URL.
from flask import Flask

# Create a Flask application instance
app = Flask(__name__) 

# Define a route for the root URL ("/")
@app.route('/')

# Define the function that will be called when this route is accessed
def hello_world():
    return "Hello, World!"

# Run the Flask application
if __name__ == '__main__':
    app.run('0.0.0.0', port=9000, debug=True)  # Set debug=True for development; it will auto-reload on code changes