import logging
from flask import Flask, request
from integration.client_integration import get_customers_by_email, get_store_by_preference

app = Flask(__name__)


@app.route('/login/<email>', methods=['GET'])
def login_cliente(email):
    try:
        response = get_customers_by_email(email)
        return response
    except Exception as e:
        print(e)


@app.route('/login/<preferencia>', methods=['GET'])
def login_cliente(preferencia):
    try:
        response = get_customers_by_email(preferencia)
        return response
    except Exception as e:
        print(e)

# @app.route('/roadmap', methods=['GET'])
# def lambda_handler():
#     try:
#         """
#         TODO
#         Determinar
#         """
#         return get_customers_by_email()
#     except Exception as e:
#         print(e)