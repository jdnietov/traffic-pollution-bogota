from pymongo import MongoClient, GEOSPHERE
from pymongo.errors import (PyMongoError, BulkWriteError)
import argparse, urllib, json
from bson import ObjectId

class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return json.JSONEncoder.default(self, o)



def writeToGeoJson(results, name):
  file = open(name, "w")
  file.write("""
  {
      "type": "FeatureCollection",
      "name": "Colombia",
      "crs": { "type": "name", "properties": { "name": "urn:ogc:def:crs:OGC:1.3:CRS84" } },
      "features": [
  """)
  
  if type(results) is dict:
    results.pop('_id', None)
    file.write(json.dumps(results))

  else:
    for result in results:
      result.pop('_id', None)
      file.write(json.dumps(result))
      file.write(',\n')

    file.write("] \n }")
    file.close()



def filterBogota(collection):
  results = collection.find({ "properties.County": "Bogotá" })
  writeToGeoJson(results, "Bogota_new.geojson")



def findSegments(db):
  geojson = db['GeoJSON']
  nrix = db['NRIX']

  result = nrix.find_one()
  nrixSegments = result['result']['segmentSpeeds'][0]['segments']
  codes = [ segment['code'] for segment in nrixSegments ]

  geoJsonSegments = geojson.find( { "properties.XDSegID" : { "$in" : codes }, "properties.County" : "Bogotá" } )
  if geoJsonSegments:
    writeToGeoJson(geoJsonSegments, "BogotaFilteredNew.geojson")



parser = argparse.ArgumentParser(description='Bulk import GeoJSON file into MongoDB')
parser.add_argument('-f', required=True, help='input file')
parser.add_argument('-s', default='localhost', help='target server name (default is localhost)')
parser.add_argument('-port', default='27017', help='server port (default is 27017)')
parser.add_argument('-d', required=True, help='target database name')
parser.add_argument('-c', required=True, help='target collection to insert to')
parser.add_argument('-u', help='username (optional)')
parser.add_argument('-p', help='password (optional)')
args = parser.parse_args()

inputfile = args.f
to_collection = args.c
to_database = args.d
to_server = args.s
to_port = args.port
db_user = args.u

if db_user is None:
  uri = 'mongodb://' + to_server + ':' + to_port +'/'
else:
#  db_password = urllib.quote_plus(args.p)
  db_password = args.p
  uri = 'mongodb://' + db_user + ':' + db_password + '@' + to_server + ':' + to_port +'/' + to_database

client = MongoClient(uri)
db = client[to_database]
collection = db[to_collection]

# filterBogota(collection)
findSegments(db)