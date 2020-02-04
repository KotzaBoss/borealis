import json
from pprint import pprint

import requests

test = requests.get('https://www.dnd5eapi.co/api')
pprint(json.loads(test.text))
