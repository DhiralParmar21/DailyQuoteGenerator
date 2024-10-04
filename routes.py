from flask import render_template, redirect, url_for, flash
from app import app, mysql
from app.forms import SubmitQuoteForm, FilterQuotesForm
from flask import send_from_directory


@app.route('/', endpoint='index')
def home():
    
    
    # Example: Fetch a quote (replace this with your actual database logic)
    quote = ["Believe in yourself!", "Unknown"]
    return render_template('index.html', quote=quote)

@app.route('/favicon.ico')
def favicon():
    return send_from_directory('static', 'favicon.ico', mimetype='image/vnd.microsoft.icon', cache_timeout=60*60*24*30)  # Cache for 30 days    

@app.route('/submit', methods=['GET', 'POST'])
def submit_quote():
    form = SubmitQuoteForm()
    if form.validate_on_submit():
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO quotes (text, author, category) VALUES (%s, %s, %s)", 
                    (form.text.data, form.author.data, form.category.data))
        mysql.connection.commit()
        cur.close()
        flash("Quote successfully submitted!", "success")
        return redirect(url_for('index'))
    
    return render_template('submit_quote.html', form=form)


@app.route('/filter', methods=['GET', 'POST'])
def filter_quotes():
    form = FilterQuotesForm()
    quotes = []
    if form.validate_on_submit():
        category = form.category.data
        mood = form.mood.data

        # Example SQL query for filtering quotes
        query = "SELECT text, author FROM quotes WHERE 1=1"
        if category != 'all':
            query += f" AND category = '{category}'"
        if mood != 'any':
            query += f" AND mood = '{mood}'"

        cur = mysql.connection.cursor()
        cur.execute(query)
        quotes = cur.fetchall()
        cur.close()

    return render_template('filter_quotes.html', form=form, quotes=quotes)

# Route to submit a quote (accessible through the link)
@app.route('/submit_quote')
def submit_quote_page():
    return redirect(url_for('submit_quote'))

# Route to filter quotes (accessible through the link)
@app.route('/filter_quotes')
def filter_quotes_page():
    return redirect(url_for('filter_quotes'))