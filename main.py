import sys
from io import BytesIO

from getting_object_parametres import get_params

import requests
from PIL import Image

import argparse as ap

parser = ap.ArgumentParser(description='Введите наименование объекта и (по желанию) координаты объекта параметром --spn')
parser.add_argument('toponym_to_find', nargs = '*')
parser.add_argument('--spn', required=False, type=float, default=0.005)
args = parser.parse_args()

map_params = get_params(' '.join(args.toponym_to_find), str(args.spn))
map_params['pt'] = map_params['ll'] + ',ya_ru'

map_api_server = "http://static-maps.yandex.ru/1.x/"
response = requests.get(map_api_server, params=map_params)

Image.open(BytesIO(response.content)).show()