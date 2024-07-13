import requests
import os
import json


def get_customers_by_email(email):
    url = f"{os.environ.get('API_URL')}/customers/details"
    listagem_clientes = requests.get(url)
    for cliente in listagem_clientes.json():
        if email == cliente['email']:
            return {
                'nome': cliente['email'],
                'preferencias': cliente['preferences'],
                'id': cliente['id']
            }
        else:
            return {
                'statusCode': 400,
                'body': 'Cliente não encontrado'
            }


def get_store_by_preference(preference):
    url = f"{os.environ.get('API_URL')}/stores/details"
    lojas_preferidas = []
    listagem_lojas = requests.get(url)
    for loja in listagem_lojas.json():
        if preference == loja['category']:
            lojas_preferidas.append({
                'nome': loja['name'],
                'abertura': loja['openingHours']
            })
    if len(lojas_preferidas) > 0:
        return lojas_preferidas
    else:
        return {
            'statusCode': 400,
            'body': 'Preferência não encontrada'
        }


def get_cashback_by_id(customer_id):
    url = f"{os.environ.get('API_URL')}/wallets/details?customerId={customer_id}"
    cashback = requests.get(url)
    if cashback.ok:
        return {
            "total": cashback['balance'],
            "total_loja": cashback['transactions']
        }
    else:
        "Erro ao buscar o cashback"