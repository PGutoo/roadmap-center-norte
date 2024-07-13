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


def get_store_by_preference(preference):
    url = f"{os.environ.get('API_URL')}/stores/details"
    loja_preferidas = []
    listagem_lojas = requests.get(url)
    for loja in listagem_lojas.json():
        if preference == loja['category']:
            return loja_preferidas.append({
                'nome': loja['name'],
                'abertura': loja['openingHours']
            })
        else:
            return {
                'statusCode': 400,
                'body': 'Cliente não encontrado'
            }
