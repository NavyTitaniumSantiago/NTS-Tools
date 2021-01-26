import json

dataArr = []


with open('routines.json') as json_file:
  r_Open =json.load(json_file)
  for item in r_Open:
    data = {'Name': item,
    'Difficulty': r_Open[item]["Difficulty Level"],
    'Focus': r_Open[item]["Focus"]}
    dataArr.append(data)

with open("routineTypes.json", "a") as outfile:
  json.dump(dataArr, outfile)
