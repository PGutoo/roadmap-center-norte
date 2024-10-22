from flask import Flask
from integration.client_integration import get_customers_by_email, get_store_by_preference, get_cashback_by_id

app = Flask(__name__)


@app.route('/status', methods=['GET'])
def status():
    return 'OK'


@app.route('/login/<email>', methods=['GET'])
def login_cliente(email):
    try:
        response = get_customers_by_email(email)
        return response
    except Exception as e:
        print(e)


@app.route('/preferencias/<preferencia>', methods=['GET'])
def preferencias(preferencia):
    try:
        response = get_store_by_preference(preferencia)
        return response
    except Exception as e:
        print(e)


@app.route('/cashback/<customer_id>', methods=['GET'])
def cashback(customer_id):
    try:
        response = get_cashback_by_id(customer_id)
        return response
    except Exception as e:
        print(e)


if __name__ == '__main__':
    app.run(debug=True)
