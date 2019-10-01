from dotenv import load_dotenv
from waqi import fetch_cities

load_dotenv()

# TODO: draw locations on OpenStreetMap (will be useful later!)

locations = fetch_cities()
print(locations)