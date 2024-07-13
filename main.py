import logging
from flask import Flask, request
from integration.client_integration import get_customers_by_email

app = Flask(__name__)


@app.route('/login/<email>', methods=['GET'])
def login_cliente(email):
    try:
        # Agora você pode acessar os dados como um objeto JSON
        response = get_customers_by_email(email)
        return response
    except Exception as e:
        print(e)


if __name__ == '__main__':
    app.run(debug=True)
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