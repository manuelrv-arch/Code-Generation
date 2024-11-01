from flask import Flask, render_template, redirect, url_for, request, flash
from extensions import db  # Import db from extensions
from forms import TransactionForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///budget.db'
db.init_app(app)  # Initialize db with app

from models import Transaction  # Import models after app and db are set up

@app.route('/')
def index():
    total_income = db.session.query(db.func.sum(Transaction.amount)).filter(Transaction.type == 'Income').scalar() or 0
    total_expenses = db.session.query(db.func.sum(Transaction.amount)).filter(Transaction.type == 'Expense').scalar() or 0
    balance = total_income - total_expenses
    transactions = Transaction.query.order_by(Transaction.date.desc()).all()
    return render_template('index.html', balance=balance, income=total_income, expenses=total_expenses, transactions=transactions)

@app.route('/add', methods=['GET', 'POST'])
def add_transaction():
    form = TransactionForm()
    if form.validate_on_submit():
        transaction = Transaction(
            amount=form.amount.data,
            type=form.type.data,
            category=form.category.data,
            description=form.description.data
        )
        db.session.add(transaction)
        db.session.commit()
        flash('Transaction added successfully', 'success')
        return redirect(url_for('index'))
    return render_template('add_transaction.html', form=form)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
