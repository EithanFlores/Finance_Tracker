import pytest
from project import generate_pie_chart, generate_bar_chart, Transaction, db, app

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client
        with app.app_context():
            db.drop_all()

def test_generate_pie_chart():
    with app.app_context():
        assert generate_pie_chart() is None or isinstance(generate_pie_chart(), str)

def test_generate_bar_chart():
    with app.app_context():
        assert generate_bar_chart() is None or isinstance(generate_bar_chart(), str)

def test_add_transaction(client):
    with app.app_context():
        transaction = Transaction(type="Income", title="Test Income", description="Test Desc", amount=100.0)
        db.session.add(transaction)
        db.session.commit()

        assert transaction in db.session

def test_delete_transaction(client):
    with app.app_context():
        transaction = Transaction(type="Expense", title="Test Expense", description="Test Desc", amount=50.0)
        db.session.add(transaction)
        db.session.commit()
        
        db.session.delete(transaction)
        db.session.commit()
        
        assert Transaction.query.get(transaction.id) is None
