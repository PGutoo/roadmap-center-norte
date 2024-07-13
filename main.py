from flask import Flask
from integration.client_integration import get_customers_by_email

app = Flask(__name__)


@app.route('/roadmap', methods=['GET'])
def lambda_handler():
    try:
        """
        TODO
        Determinar         
        """
        return get_customers_by_email()
    except Exception as e:
        print(e)