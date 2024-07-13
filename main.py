import logging
from fastapi import FastAPI
from fastapi.responses import JSONResponse

from integration.client_integration import get_customers_by_email

app = FastAPI()


@app.get("/login/{email}", response_class=JSONResponse)
def login_cliente(email: str):
    try:
        # Agora você pode acessar os dados como um objeto JSON
        # logging.info("Verificando cliente no Clube")
        # response = get_customers_by_email(email)
        return "OK"
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