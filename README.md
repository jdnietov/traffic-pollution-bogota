# Aeolus

Manager for MongoDB traffic and pollution databases in Python 3.6.

## Dependencies

``pip3 install --user python-dotenv``

pip3 install --upgrade imutils
pip3 install --upgrade scikit-learn
pip3 install --upgrade matplotlib

## Sources 

- Air pollution information was obtained from http://aqicn.org/city/colombia/bogota

Covering the following Bogotá areas:
- Guaymaral 
- Suba
- Usaquén
- Las Ferias
- Fontibón
- Centro de Alto Rendimiento
- US Consulate
- Puente Aranda
- MinAmbiente
- Kennedy
- Carvajal
- Tunal
- San Cristóbal

## Files

### `db/traffic/scripts`
En db/traffic/scripts se encuentran dos scripts importantes:
- `geojson-mongo-import.py`: importar un JSON de tamaño indefinido en una base de datos de Mongo previamente creada.
- `geomongo.py`: extraer información de una base de datos de Mongo para copiarla en disco en formato GeoJSON.