import requests
import os


def get_customers_by_email():
    url = f"{os.environ.get('API_URL')}/customers/details"
    return url