import json
from pprint import pprint

json_data = json.loads(open('data.json').read())

for obj in json_data:
	print("\n\n"+obj["Film"])

	if (obj["Number_of_Theatres_in_Opening_Weekend"] != ""):
		obj["Number_of_Theatres_in_Opening_Weekend"] = float(obj["Number_of_Theatres_in_Opening_Weekend"].replace(',',''))
	else: 
		obj["Number_of_Theatres_in_Opening_Weekend"] = None
'''
	if (obj["Worldwide"] != ""):
		obj["Worldwide"] = float(obj["Worldwide"].replace(',',''))
	else: 
		obj["Worldwide"] = None

	if (obj["Opening_Weekend"] != ""):
		obj["Opening_Weekend"] = float(obj["Opening_Weekend"].replace(',',''))
	else: 
		obj["Opening_Weekend"] = None

	if (obj["Budget"] != ""):
		obj["Budget"] = float(obj["Budget"].replace(',',''))
	else:
		obj["Budget"] = None

	if (obj["Box_Office_Avg_Opening_Wknd"] != ""):
		obj["Box_Office_Avg_Opening_Wknd"] = float(obj["Box_Office_Avg_Opening_Wknd"].replace(',',''))
	else:
		obj["Box_Office_Avg_Opening_Wknd"] = None

	if (obj["Foreign_Gross"] != ""):
		obj["Foreign_Gross"] = float(obj["Foreign_Gross"].replace(',',''))
	else:
		obj["Foreign_Gross"] = None

	if (obj["Domestic_Gross"] != ""):
		obj["Domestic_Gross"] = float(obj["Domestic_Gross"].replace(',',''))
	else:
		obj["Domestic_Gross"] = None

	if (obj["Market_Profitability"] != ""):
		obj["Market_Profitability"] = obj["Market_Profitability"].replace('%','')
		obj["Market_Profitability"] = float(obj["Market_Profitability"].replace(',',''))
	else:
		obj["Market_Profitability"] = None
		'''
with open('cleaner_data.json', 'w') as outfile:
    json.dump(json_data, outfile)
