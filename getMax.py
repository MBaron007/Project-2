# import json
# from pprint import pprint
# json_data=open('votes.json')

# playersArray = []
# player = {}
# checkedPlayers = []

# data = json.load(json_data)
# for d in data:
# 	name = d['Name']
# 	finalYear = 0
# 	percentage = 0
# 	if name not in checkedPlayers:
# 		finalYear = d['Year']
# 		percentage = d['pct']
# 		checkedPlayers.append(name)
# 		player = { "Name" : name, "Final_Year" : finalYear, "Percentage" : percentage}
# 		playersArray.append(player)

# with open('officialPlayer.json','w') as outfile:
# 	print "Writing to file..."
# 	json.dump(playersArray, outfile)
# 	print "Written"


#pprint(playersArray)

import json
from pprint import pprint
json_data = open('data.json')


checkedPlayers = []
playersArray = []
player = {}

data = json.load(json_data)

lenData = len(data)

maxWeekend = 0
maxWorld = 0
maxOpen = 0
maxAud = 0
maxMar = 0
maxBox = 0
maxBud = 0
maxFor = 0
maxCrit = 0
maxDom = 0

for d in data:
	#print d
	if d['Number_of_Theatres_in_Opening_Weekend'] > maxWeekend:
		maxWeekend = d['Number_of_Theatres_in_Opening_Weekend']
	if d['Worldwide'] > maxWorld:
		maxWorld = d['Worldwide']
	if d['Opening_Weekend'] > maxOpen:
		maxOpen = d['Opening_Weekend']
	if d['Audience_Score'] > maxAud:
		maxAud = d['Audience_Score']
	if d['Market_Profitability'] > maxMar:
		maxMar = d['Market_Profitability']
	if d['Box_Office_Avg_Opening_Wknd'] > maxBox:
		maxBox = d['Box_Office_Avg_Opening_Wknd']
	if d['Budget'] > maxBud:
		maxBud = d['Budget']
	if d['Foreign_Gross'] > maxFor:
		maxFor = d['Foreign_Gross']
	#if d['Critics_Score'] > maxCrit:
	#	maxCrit = d['Critics_Score']
	if d['Domestic_Gross'] > maxDom:
		maxDom = d['Domestic_Gross']


print maxWeekend
print maxWorld
print maxOpen
print maxAud
print maxMar
print maxBox
print maxBud
print maxFor
print maxCrit
print maxDom



# 	position = ""
# 	name = d['Name']
# 	finalYear = d['Final_Year']
# 	percentage = d['Percentage']
# 	stats = {}
# 	isPlayer = False

# 	if name not in checkedPlayers:
# 		for a in otherData: 
# 				if a['Name'] == name:
# 					position = a['position']
# 					isPlayer = True
# 				if isPlayer:
# 					if d['Final_Year'] < 2014:
# 						if position == 'P':
# 							#print "here: " + a['Name']
# 							stats['W'] = a['W']
# 							stats['L'] = a['L']
# 							stats['ERA'] = a['ERA']
# 							stats['WHIP'] = a['WHIP']
# 							stats['GS'] = a['GS']
# 							stats['SV'] = a['SV']
# 							stats['IP'] = a['IP']
# 							stats['SO'] = a['SO']
# 						else:
# 							stats['Yrs'] = a['Yrs']
# 							stats['AB'] = a['AB']
# 							stats['R'] = a['R']
# 							stats['H'] = a['H']
# 							stats['HR'] = a['HR']
# 							stats['RBI'] = a['RBI']
# 							stats['SB'] = a['SB']
# 							stats['BB'] = a['BB']
# 							stats['BA'] = a['BA']
# 							stats['OBP'] = a['OBP']
# 							stats['SLG'] = a['SLG']
# 							stats['OPS'] = a['OPS']

# 					break

# 		player = { "Name" : name, "Final_Year" : finalYear, "Percentage" : percentage, "Stats" : stats, "Position" : position}
# 		playersArray.append(player)
# 		checkedPlayers.append(name)
# 		stats = {}
# 		lenData = lenData - 1
# 		print lenData

# with open('steph.json','w') as outfile:
#  	print "Writing to file..."
#  	json.dump(playersArray, outfile)
#  	print "Written"