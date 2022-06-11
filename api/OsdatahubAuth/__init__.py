
import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    return func.HttpResponse(
            "PRET CRAWL 2",
            status_code=200
    )

    from urllib import requests, parse
    import logging

    logging.info('Python HTTP trigger function processed a request.')
    data = req.get_json()
    logging.info(data)
    key = data["key"]
    secret = environ.get("OS_API_SECRET")
    # logging.info(secret)
    auth = (key, secret)
    url = 'https://api.os.uk/oauth2/token/v1'

    data = parse.urlencode({
            "grant_type": "client_credentials"
        }).encode()

    auth = f"Basic " + base64.b64encode(f"{key}:{secret}".encode("ascii")).decode()
    logging.info(auth)

    req =  request.Request(url, data=data) # this will make the method "POST"
    req.add_header("Authorization", auth)
    req.add_header("Content-Type", "application/x-www-form-urlencoded")
    resp = request.urlopen(req)

    content =  resp.read().decode("utf-8")
    logging.info(content)
    if resp.getcode() == 200:
        return func.HttpResponse(
            content,
            status_code=200
        )
    else:
        raise Exception("Something has gone wrong")
