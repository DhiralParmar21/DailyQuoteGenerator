from flask import Flask
from flask_mysqldb import MySQL
from flask_wtf.csrf import CSRFProtect

# Initialize the Flask application
app = Flask(__name__)

# Configure the app
app.config['SECRET_KEY'] = 'larihd21'  # Secret key for security (CSRF, sessions, etc.)
app.config['MYSQL_HOST'] = 'Dhiral'  # Database host, e.g., localhost
app.config['MYSQL_USER'] = 'root'  # MySQL username
app.config['MYSQL_PASSWORD'] = 'DF21'  # MySQL password
app.config['MYSQL_DB'] = 'quote_db'  # Database name
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'  # To return results as a dictionary

# Initialize the MySQL extension
mysql = MySQL(app)

# Enable CSRF protection for forms
csrf = CSRFProtect(app)

# Import routes (you will define routes in a separate file)
from app import routes
