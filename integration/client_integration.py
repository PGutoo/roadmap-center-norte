import requests
import os


def get_customers_by_email(email):
    url = f"{os.environ.get('API_URL')}/customers/details"
    listagem_clientes = requests.get(url)
    for cliente in listagem_clientes.json():
        if email == cliente['email']:
            return {
                'nome': cliente['email'],
                'preferencias': cliente['preferences']
            }
        else:
            return {
                'statusCode': 400,
                'body': 'Cliente não encontrado'
            }
