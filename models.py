from extensions import db  # Import db from extensions
from datetime import datetime

class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Float, nullable=False)
    type = db.Column(db.String(10), nullable=False)  # 'Income' or 'Expense'
    category = db.Column(db.String(20), nullable=False)
    description = db.Column(db.String(100))
    date = db.Column(db.DateTime, default=datetime.utcnow)
