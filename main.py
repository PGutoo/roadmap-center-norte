import logging
import json
from flask import Flask, request
from integration.client_integration import get_customers_by_email

app = Flask(__name__)


@app.route('/login/<email>', methods=['GET'])
def login_cliente(email):
    try:
        data = request.data.decode('utf-8')
        json_data = json.loads(data)

        # Agora você pode acessar os dados como um objeto JSON
        email = json_data.get('email')
        logging.info("Verificando cliente no Clube")
        response = get_customers_by_email(email)
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