from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField
from wtforms.validators import DataRequired, Length

# Quote submission form
class SubmitQuoteForm(FlaskForm):
    text = StringField(
        'Quote', 
        validators=[
            DataRequired(message="The quote text is required."), 
            Length(min=5, max=500, message="Quote must be between 5 and 500 characters.")
        ],
         render_kw={"class": "border border-gray-300 rounded-lg p-2 w-full"}
    )
    author = StringField(
        'Author', 
        validators=[
            DataRequired(message="The author's name is required."),
            Length(max=100, message="Author's name must be 100 characters or less.")
        ],
        render_kw={"class": "border border-gray-300 rounded-lg p-2 w-full"}
    )
    category = SelectField(
        'Category',
        choices=[
            ('inspiration', 'Inspiration'),
            ('motivation', 'Motivation'),
            ('life', 'Life'),
            ('love', 'Love'),
            ('wisdom', 'Wisdom')
        ],
        validators=[DataRequired(message="Please choose a category.")]
    )
    
     # Add the mood field here if it's part of the form
    mood = SelectField(
        'Mood',
        choices=[
            ('happy', 'Happy'),
            ('thoughtful', 'Thoughtful'),
            ('sad', 'Sad'),
            ('excited', 'Excited')
        ],
        validators=[DataRequired()]
    )
    
    submit = SubmitField('Submit Quote', render_kw={"class": "bg-blue-500 text-white py-2 px-4 rounded-lg hover:bg-blue-600 focus:outline-none focus:ring-2 focus:ring-blue-300" })


# Filter quotes form
class FilterQuotesForm(FlaskForm):
    category = SelectField(
        'Category',
        choices=[
            ('all', 'All Categories'),
            ('inspiration', 'Inspiration'),
            ('motivation', 'Motivation'),
            ('life', 'Life'),
            ('love', 'Love'),
            ('wisdom', 'Wisdom')
        ],
        default='all'
    )
    mood = SelectField(
        'Mood',
        choices=[
            ('any', 'Any Mood'),
            ('happy', 'Happy'),
            ('thoughtful', 'Thoughtful'),
            ('sad', 'Sad'),
            ('excited', 'Excited')
        ],
        default='any'
    )
    submit = SubmitField('Filter Quotes', render_kw={"class": "bg-blue-500 text-white py-2 px-4 rounded-lg hover:bg-blue-600 focus:outline-none focus:ring-2 focus:ring-blue-300"})
