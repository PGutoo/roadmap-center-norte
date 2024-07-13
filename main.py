import logging
from flask import Flask, request
from integration.client_integration import get_customers_by_email

app = Flask(__name__)


@app.route('/login/<email>', methods=['GET'])
def login_cliente(email):
    try:
        data = request.args['email']
        # Agora você pode acessar os dados como um objeto JSON
        logging.info("Verificando cliente no Clube")
        response = get_customers_by_email(data)
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