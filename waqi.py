import os
import json
import pymongo
from urllib.request import urlopen

localities = [
    'guaymaral',
    'suba',
    'usaquen',
    'las-ferias',
    'fontibon',
    'centro-de-alto-rendimiento',
    'us-consulate',
    'puente-aranda',
    'minambiente',
    'kennedy',
    'carvajal',
    'tunal',
    'san-cristobal'
]

def fetch_cities():
    locations = []
    try:
        for l in localities:
            print(f'Fetching info from {l}')
            url = urlopen(f"https://api.waqi.info/feed/colombia/bogota/{l}/?token={os.environ.get('WAQI_KEY')}")
            
            try:
                obj = json.load(url)
                locations.append(obj["data"]["city"]["geo"])

            except ValueError:
                print("Error handling JSON")

    except ValueError:
        print("Error in WAQI request")
    
    return locations