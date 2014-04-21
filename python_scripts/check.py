from urllib2 import Request, urlopen, URLError
import json
import re
import urllib2
import time

from pprint import pprint

json_data = json.loads(open('data.json').read())

j = 0
length = len(json_data)
for obj in json_data:
	if (obj["Foreign_Gross"] == None or obj["Foreign_Gross"] == 0):
		obj["Foreign_Gross"] = None
		obj["Worldwide"] = None
		obj["Market_Profitability"] = None
	elif obj["Budget"] == 0:
		obj["Budget"] = None


with open('data.json', 'w') as outfile:
    json.dump(json_data, outfile)
