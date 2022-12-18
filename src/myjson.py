#!/usr/local/bin/python3
import json


with open('list.json') as json_file:  
   data = json.load(json_file)
   print json.dumps(parsed, indent=4, sort_keys=True)
