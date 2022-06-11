import logging
import requests
from os import environ
import json

import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    data = req.get_json()
    logging.info(data)
    key = data["key"]
    secret = environ.get("OS_API_SECRET")
    # logging.info(secret)
    auth = (key, secret)

    response = requests.post(
        url='https://api.os.uk/oauth2/token/v1',
        auth=auth,
        data={
            "grant_type": "client_credentials"
        }
    )
    logging.info(response.content)

    if response.status_code == 200:
        return func.HttpResponse(
            json.dumps(response.content.decode("utf-8")),
            status_code=200
        )
    else:
        return func.HttpResponse(
            response.content.decode("utf-8"),
            status_code=response.status_code
        )