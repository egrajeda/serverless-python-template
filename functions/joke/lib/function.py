import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../venv/lib/python3.6/site-packages"))

import requests


def main(event, context):
    response = requests.get("https://api.icndb.com/jokes/random").json()
    return {
        "statusCode": 200,
        "body": response["value"]["joke"]
    }
