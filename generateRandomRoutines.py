import json
import randomString
import random

difficultyLevel = ['Beginner', 'Intermediate', 'Advanced']
focus = ['General Fitness', 'Weightloss', 'Strength', 'Abs']
data = {}


def generate_set():
	set = {}
	set['Exercise'] = random.choice(list(exOpened.keys()))
	set['defaultWeight'] = set['customWeight'] = random.choice([5, 10, 15])
	set['defaultRepCD'] = set['customRepCD'] = 40
	set['defaultSetCD'] = set['customSetCD'] = 60
	set['defaultReps'] = set['customReps'] = random.choice([3,5,8,10,12])
	increaseWeight = 5
	increaseFrequency = 30
	increaseStrategy = {'increaseBy': increaseWeight, 'increaseWhen': increaseFrequency}
	set['defaultIncreaseStrategy'] = set['customIncreaseStrategy'] = increaseStrategy
	return set
	
def generate_day():
	day = {}
	numOfSets = random.randrange(0, 7)
	day['Number of Sets'] = numOfSets
	day['Is rest day'] = False
	day['Sets'] = []
	if numOfSets == 0:
		day['Is rest day'] = True
		return day
	while numOfSets>0:
		day['Sets'].append(generate_set())
		numOfSets-=1
	return day
	
def generate_cycle(cycleLength):
	cycle = {}
	cycle['Length'] = cycleLength
	cycle['Days'] = []
	for i in range(0, cycleLength):
		cycle['Days'].append(generate_day())
	return cycle

def generate_routine(routineName):
	data[routineName] = {}
	routine = data[routineName]
	routine['Difficulty Level'] = random.choice(difficultyLevel)
	routine['Focus'] = random.choice(focus)
	routine['Total Length'] = random.randrange(7, 31)
	routine['Number of Cycles'] = random.randrange(1,5)
	routine['Cycles'] = []
	daysToFill = routine['Total Length']
	cyclesToFill = routine['Number of Cycles']
	while daysToFill>0:
		maxCycleLength = daysToFill-cyclesToFill if cyclesToFill >1 else daysToFill
		minCycleLength = 1 if cyclesToFill>1 else daysToFill
		cycleLength = random.randrange(minCycleLength, maxCycleLength+1)
		data[routineName]['Cycles'].append(generate_cycle(cycleLength))
		daysToFill-=cycleLength
		cyclesToFill-=1


	

				
	
with open('exercises.json') as json_file:
	exOpened = json.load(json_file)
	#print(random.choice(list(exOpened.keys())))
	for i in range(0, 15):
		routineName = randomString.gen_word(3, 5)
		generate_routine(routineName)
	with open("routines.json", 'w') as outfile:
		json.dump(data, outfile)
	



	


	