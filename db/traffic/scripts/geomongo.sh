#!/bin/bash
# server set to default (localhost)

file="Colombia.geojson"
db="NRIX"
collection="GeoJSON"
user="jdnietov"
password="nrix2019*"

#python geojson-mongo-import.py -f $file -d $db -c $collection -u $user -p $password > output.log
python3 geomongo.py -f $file -d $db -c $collection -u $user -p $password