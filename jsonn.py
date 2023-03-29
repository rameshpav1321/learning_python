# *** JSON parsing stuff ***

import json
from urllib.request import urlopen

# handling json data from files
with open('learning_python/states.json') as f:
    data=json.load(f)

for state in data['states']:
    # print(state["name"],state["abbreviation"])
    del state['area_codes']

with open('learning_python/new_states.json','w') as f:
    json.dump(data,f,indent=2)

# handling json data from dummy api endpoint
with urlopen('https://dummyjson.com/carts?limit=3') as response:
    source=response.read()

data=json.loads(source)
# print(json.dumps(data,indent=2))

for product in data['carts'][2]:
    print(product)