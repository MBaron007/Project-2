from urllib2 import Request, urlopen, URLError
import json
import re
import urllib2
import time

from pprint import pprint

json_data = json.loads(open('data.json').read())

i = 0
length = len(json_data)
for obj in json_data:
	title = obj["Film"]
	title = re.sub(' ', '+', title.rstrip())
	url = 'http://api.rottentomatoes.com/api/public/v1.0/movies.json?apikey=wk8hj2gxw4dqeef5sufjrq9n&q='+title
	try:
		request = json.load(urllib2.urlopen(url))
		try:
		    obj["id"] = request["movies"][0]["id"]
		except IndexError:
		    obj["Images"] = []
		    print "IndexError - " + title
	except URLError:
		obj["Images"] = []
		print "URLError - " + title
	print(str(i)+"/"+str(length))
	i += 1
	time.sleep(.1)

with open('result.json', 'w') as outfile:
    json.dump(json_data, outfile)


#try:
#	response = urlopen(request)
#	kittens = response.read()
#	print kittens[559:1000]
#except URLError, e:
#    print 'No kittez. Got an error code:', e