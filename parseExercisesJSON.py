import json

data = {}
data['Muscle Groups'] = {}
data['Equipment Types'] = {}

with open('exercises.json') as json_file:
	exOpened = json.load(json_file)
	for item in exOpened:
		entry = exOpened[item]
		if entry['Muscle Group'] in data['Muscle Groups']:
			data['Muscle Groups'][entry['Muscle Group']].append(entry['Exercise Name'])
		else:
			data['Muscle Groups'][entry['Muscle Group']] = [entry['Exercise Name']]
		equipmentArr = entry['Equipment'].split('/')
		for tool in equipmentArr:
			tool = tool.strip()
			if tool in data['Equipment Types']:
				data['Equipment Types'][tool].append(entry['Exercise Name'])
			else:
				data['Equipment Types'][tool] = [entry['Exercise Name']]
	with open("exerciseTypes.json", 'a') as outfile:
		json.dump(data, outfile)