from flask_wtf import FlaskForm
from wtforms import FloatField, SelectField, StringField, SubmitField
from wtforms.validators import DataRequired

class TransactionForm(FlaskForm):
    amount = FloatField('Amount', validators=[DataRequired()])
    type = SelectField('Type', choices=[('Income', 'Income'), ('Expense', 'Expense')], validators=[DataRequired()])
    category = SelectField('Category', choices=[('Food', 'Food'), ('Rent', 'Rent'), ('Entertainment', 'Entertainment'), ('Pay', 'Pay')], validators=[DataRequired()])
    description = StringField('Description')
    submit = SubmitField('Add Transaction')
