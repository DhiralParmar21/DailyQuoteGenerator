from app import mysql

# Function to add a new quote
def add_quote(text, author, category):
    cur = mysql.connection.cursor()
    query = "INSERT INTO quotes (text, author, category) VALUES (%s, %s, %s)"
    cur.execute(query, (text, author, category))
    mysql.connection.commit()
    cur.close()

# Function to fetch a random quote for the homepage
def get_random_quote():
    cur = mysql.connection.cursor()
    cur.execute("SELECT text, author FROM quotes ORDER BY RAND() LIMIT 1")
    random_quote = cur.fetchone()
    cur.close()
    return random_quote

# Function to filter quotes by category and mood
def filter_quotes(category=None, mood=None):
    cur = mysql.connection.cursor()
    
    # Build the query dynamically based on the provided filters
    query = "SELECT text, author FROM quotes WHERE 1=1"
    
    if category and category != 'all':
        query += " AND category = %s"
    
    if mood and mood != 'any':
        query += " AND mood = %s"

    # Execute query with parameters if they exist
    cur.execute(query, (category, mood))
    quotes = cur.fetchall()
    cur.close()
    
    return quotes

# Function to retrieve all categories (for use in forms)
def get_categories():
    cur = mysql.connection.cursor()
    cur.execute("SELECT DISTINCT category FROM quotes")
    categories = cur.fetchall()
    cur.close()
    return categories

# Function to retrieve all moods (for use in forms)
def get_moods():
    cur = mysql.connection.cursor()
    cur.execute("SELECT DISTINCT mood FROM quotes")
    moods = cur.fetchall()
    cur.close()
    return moods
