import logging
from fastapi import FastAPI

from integration.client_integration import get_customers_by_email

app = FastAPI()


@app.get('/login/{email}')
def login_cliente(email):
    try:
        # Agora você pode acessar os dados como um objeto JSON
        logging.info("Verificando cliente no Clube")
        # response = get_customers_by_email(email)
        return {
            'statusCode': 200,
            'body': email
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