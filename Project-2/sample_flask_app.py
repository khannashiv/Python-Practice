# This is a simple Flask application that returns "Hello, World!" when accessed at the root URL.
from flask import Flask

# The line app = Flask(__name__) creates a new instance of the Flask web application. 
# Here, Flask is a class provided by the Flask framework, and __name__ is a special Python variable that holds the name of the current module.
# Passing __name__ to the Flask constructor helps Flask determine the root path of our application, 
# which it uses to locate resources such as templates and static files. 
# The resulting app object acts as the central registry for our web application, 
# allowing you to define routes, configure settings, and manage the application's lifecycle. 
# This line is typically found near the top of a Flask application and is required to start building and running your web server.

# Create a Flask application instance
app = Flask(__name__) 

# The line @app.route('/') is a decorator in Flask that associates a specific URL path—in this case, 
# the root URL '/'— with a view function. When a user accesses the root of your web application (for example, http://localhost:9000/), 
# Flask will call the function immediately following this decorator to handle the request.
# This decorator simplifies the process of mapping URLs to Python functions, 
# making it easy to define what content or response should be returned for different routes in your application.
# By using @app.route('/'), you are telling Flask, "Whenever someone visits the homepage, "
# "run the following function and return its result as the response." 
# This is a core concept in building web applications with Flask.

# Define a route for the root URL ("/")
@app.route('/')

# The function hello_world() is a simple Python function that, when called, returns the string "Hello, World!".
# In the context of a Flask application, this function is typically used as a view function, 
# meaning it defines the response that will be sent back to the client when a specific route is accessed.
# When this function is linked to a route (for example, using the @app.route('/') decorator), 
# Flask will execute hello_world() whenever a user visits that route. 
# The returned string is then sent as the HTTP response body, so the user will see "Hello, World!" displayed in their browser. 

# Define the function that will be called when this route is accessed
def hello_world():
    return "Hello, World!"

# This code block is responsible for starting the Flask web application when the script is executed directly. 
# The line if __name__ == '__main__': checks whether the script is being run as the main program, 
# rather than being imported as a module. If this condition is true, the code inside the block will execute.

# The line app.run('0.0.0.0', port=9000, debug=True) launches the Flask development server. 
# The argument '0.0.0.0' tells Flask to listen on all available network interfaces, 
# making the app accessible from other devices on the same network. 
# The port=9000 argument specifies that the server should listen on port 9000 instead of the default port 5000. 
# The debug=True option enables debug mode, which provides helpful error messages and automatically reloads the server when code changes are detected.
# This setup is useful for development and testing, but it is not recommended for production environments.

# Run the Flask application
if __name__ == '__main__':
    app.run('0.0.0.0', port=9000, debug=True)  # Set debug=True for development; it will auto-reload on code changes
