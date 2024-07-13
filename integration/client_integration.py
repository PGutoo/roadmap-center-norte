import requests
import os


def get_customers_by_email(email):
    url = f"{os.environ.get('API_URL')}/customers/details"
    listagem_clientes = requests.get(url)
    for cliente in listagem_clientes:
        if email == cliente.get('email'):
            return {
                'nome': cliente.get('firstName'),
                'preferencias': cliente.get('preferences')
            }
        else:
            return {
                'statusCode': 400,
                'body': 'Cliente não encontrado'
            }
