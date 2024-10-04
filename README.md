# Daily Quote Generator

## Project Overview

The **Daily Quote Generator** is a web application that displays a different inspirational or thought-provoking quote each day. It also allows users to submit their own quotes and filter quotes by category or mood. The project is built using **Python Flask** for the backend, **MySQL** for the database, and standard web technologies (HTML, CSS, JavaScript) for the frontend.

## Features

- Display a random inspirational quote on the homepage.
- Allow users to submit their own quotes.
- Filter quotes based on category or mood.
- Store and retrieve quotes from a MySQL database.

## Technology Stack

- **Backend**: Python (Flask)
- **Frontend**: HTML, CSS, JavaScript (with jQuery)
- **Database**: MySQL
- **Forms**: Flask-WTF (WTForms for validation)

## Prerequisites

Before running the project, ensure you have the following installed:

- Python 3.8+
- MySQL
- `pip` for managing Python packages

## Installation Instructions

1. **Clone the repository**:

    ```bash
    git clone https://github.com/yourusername/daily-quote-generator.git
    cd daily-quote-generator
    ```

2. **Set up a virtual environment**:

    ```bash
    python3 -m venv venv
    source venv/bin/activate    # On macOS/Linux
    venv\Scripts\activate       # On Windows
    ```

3. **Install the project dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

4. **Set up the MySQL database**:

    - Create a new database in MySQL called `daily_quote_generator
    `.
    - Run the following SQL script to create the necessary tables:

      ```sql
      CREATE DATABASE daily_quote_generator;

      USE daily_quote_generator;

      CREATE TABLE quotes (
          id INT AUTO_INCREMENT PRIMARY KEY,
          text VARCHAR(500) NOT NULL,
          author VARCHAR(100) NOT NULL,
          category VARCHAR(100),
          mood VARCHAR(100) DEFAULT 'any',
          created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP 
      );
      ```

5. **Configure MySQL connection**:

   In `app/__init__.py`, update the MySQL configurations with your database credentials:

   ```python
   app.config['MYSQL_HOST'] = 'localhost'
   app.config['MYSQL_USER'] = 'root'
   app.config['MYSQL_PASSWORD'] = 'DF21'
   app.config['MYSQL_DB'] = 'daily_quote_generator'
