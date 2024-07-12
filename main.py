from flask import Flask, request


app = Flask(__name__)

@app.route('/roadmap', methods=['GET'])
def lambda_handler():
    try:
        return {
            "statusCode": 200,
            "body": "Hello World"
        }
    except Exception as e:
        print(e)