import csv
import json

data = {}
#Exercise.csv needs to be in the following format:
#Exercise, MuscleGroup, "Type1, Type2, Type3", Focus, "How To", Equipment Needed, img url, video url, \n
with open("exercise.csv") as ex:
	for row in csv.reader(ex):
		print(row)
		data[row[0]] = {}
		data[row[0]]['Exercise Name'] = row[0]
		data[row[0]]['Muscle Group'] = row[1]
		data[row[0]]['Type'] = []
		for type in row[2].split(','):
			data[row[0]]['Type'].append(type.strip())
		data[row[0]]['Focus'] = row[3]		
		data[row[0]]['Execution'] = row[4]
		data[row[0]]['Equipment'] = row[5]
		data[row[0]]['Image URL'] = row[6]
		data[row[0]]['Video URL'] = row[7]
	with open("exercises.json", 'a') as outfile:
		json.dump(data, outfile)