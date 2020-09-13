from requests import get
import json


def convert_fields_to_float(game):
    game['savings'] = float(game.get('savings'))
    game['salePrice'] = float(game.get('salePrice'))
    game['normalPrice'] = float(game.get('normalPrice'))
    return game


def lambda_handler(event, context):
    params = {'pageSize': 10}
    game_api_response = get("https://www.cheapshark.com/api/1.0/deals", params=params)
    games = json.loads(game_api_response.content)
    return list(map(convert_fields_to_float, games))
