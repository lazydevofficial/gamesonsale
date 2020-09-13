from datetime import datetime

from requests import get
import json
from uuid import uuid4


def create_payload(game, brl):
    return {
        'id': str(uuid4()),
        'title': game.get("title"),
        'normalPrice': "{:.2f}".format(game.get('normalPrice') * brl),
        'salePrice': "{:.2f}".format(game.get('salePrice') * brl),
        'timestamp': datetime.now().isoformat()
    }


def lambda_handler(event, context):
    params = {'base': 'USD'}
    currency_api_response = get("https://api.exchangeratesapi.io/latest", params=params)
    return create_payload(event, json.loads(currency_api_response.content).get('rates').get('BRL'))
