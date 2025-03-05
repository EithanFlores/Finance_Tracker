import os
import matplotlib.pyplot as plt
import io
import base64
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Transaction Model
class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(10), nullable=False)  # "Income" or "Expense"
    title = db.Column(db.String(50), nullable=False)  # Added Title field
    description = db.Column(db.String(100), nullable=False)
    amount = db.Column(db.Float, nullable=False)

with app.app_context():
    db.create_all()

# Function to Generate Pie Chart (Income vs Expense)
def generate_pie_chart():
    transactions = Transaction.query.all()
    total_income = sum(t.amount for t in transactions if t.type == "Income")
    total_expense = sum(t.amount for t in transactions if t.type == "Expense")

    if total_income == 0 and total_expense == 0:
        return None  # Prevent NaN Error

    labels = ["Income", "Expense"]
    values = [total_income, total_expense]
    colors = ["#28a745", "#dc3545"]

    fig, ax = plt.subplots()
    ax.pie(values, labels=labels, autopct="%1.1f%%", colors=colors, startangle=90)
    ax.set_title("Income vs Expenses")

    img = io.BytesIO()
    plt.savefig(img, format="png")
    img.seek(0)
    return base64.b64encode(img.getvalue()).decode()

# Function to Generate Bar Chart (Spending Categories)
def generate_bar_chart():
    transactions = Transaction.query.filter_by(type="Expense").all()
    
    if not transactions:
        return None  # No data to show
    
    categories = [t.title for t in transactions]
    amounts = [t.amount for t in transactions]

    fig, ax = plt.subplots()
    ax.bar(categories, amounts, color="red")
    ax.set_title("Spending Breakdown")
    ax.set_xlabel("Category")
    ax.set_ylabel("Amount ($)")
    plt.xticks(rotation=45)

    img = io.BytesIO()
    plt.savefig(img, format="png")
    img.seek(0)
    return base64.b64encode(img.getvalue()).decode()

@app.route('/')
def index():
    filter_type = request.args.get('filter', 'all')

    if filter_type == "income":
        transactions = Transaction.query.filter_by(type="Income").all()
    elif filter_type == "expense":
        transactions = Transaction.query.filter_by(type="Expense").all()
    else:
        transactions = Transaction.query.all()

    total_income = sum(t.amount for t in transactions if t.type == "Income")
    total_expense = sum(t.amount for t in transactions if t.type == "Expense")
    balance = total_income - total_expense

    pie_chart = generate_pie_chart()
    bar_chart = generate_bar_chart()

    return render_template("index.html", transactions=transactions, balance=balance, pie_chart=pie_chart, bar_chart=bar_chart, filter_type=filter_type)

@app.route('/add', methods=['GET', 'POST'])
def add_transaction():
    if request.method == 'POST':
        type_ = request.form.get("type")
        title = request.form.get("title")
        description = request.form.get("description")
        amount = float(request.form.get("amount"))

        new_transaction = Transaction(type=type_, title=title, description=description, amount=amount)
        db.session.add(new_transaction)
        db.session.commit()
        return redirect(url_for("index"))
    
    return render_template("add_transaction.html")

@app.route('/delete/<int:id>')
def delete_transaction(id):
    transaction = Transaction.query.get_or_404(id)
    db.session.delete(transaction)
    db.session.commit()
    return redirect(url_for("index"))

def main():
    app.run(debug=True)

if __name__ == '__main__':
    main()
