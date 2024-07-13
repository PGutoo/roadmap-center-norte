import logging
from flask import Flask, request
from integration.client_integration import Integration

app = Flask(__name__)


@app.route('/login/<email>', methods=['GET'])
def login_cliente(email):
    try:
        integration = Integration()
        integration.get_customers_by_email(email)
        # Agora você pode acessar os dados como um objeto JSON
        # response = get_customers_by_email(email)
        return {
            'statusCode': 200,
            'body': "Hello"
        }
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