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
	del obj["Genre"]
	try:
		request = json.load(urllib2.urlopen(url))
		time.sleep(.1)
		self_link = request["movies"][0]["links"]["self"] + "?apikey=wk8hj2gxw4dqeef5sufjrq9n"
		try: 
			request2 = json.load(urllib2.urlopen(self_link))
			obj["Genres"] = request2["genres"]
			print obj["Genres"]
		except IndexError:
			obj["Genres"] = []
			print "No Genres field for " + title
		except URLError:
			obj["Genres"] = []
			print "Detailed URLError - " + title
	except URLError:
		obj["Genres"] = []
		print "URLError - " + title
	except IndexError:
		obj["Genres"] = []
		print "URLError - " + title
	print(str(i)+"/"+str(length))
	i += 1
	time.sleep(.1)

with open('result_with_genres.json', 'w') as outfile:
    json.dump(json_data, outfile)
