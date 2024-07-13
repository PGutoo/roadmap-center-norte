import logging
from fastapi import FastAPI

from integration.client_integration import get_customers_by_email

app = FastAPI()


@app.get("/login/{int:email}")
def login_cliente(email: int):
    try:
        # Agora você pode acessar os dados como um objeto JSON
        # logging.info("Verificando cliente no Clube")
        # response = get_customers_by_email(email)
        return {
            "statusCode": 200,
            "body": "Hello, World!"
        }
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