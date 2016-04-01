# from csvToJson import *
# csvToJson("pds.csv", "pds.json")

import json

with open('pds.json') as data_file:    
	data = json.load(data_file)

import csv
c = csv.writer(open("pdsEdited.csv", "wb"))

cleanData = [{}]

for row in data:
	temp = {}
	for item in row.items():
		# # Remove - from SSN
		# if item[0] == "SSN": 
		# 	try:
		# 		item[1] = item[1].split('-')[0]
		# 	except:
		# 		pass
		if item[1] == "NULL":
			temp[item[0]] = ""
			continue

		if item[0] == "Gender":
			if item[1] == "0":
				temp[item[0]] = "Female"
			elif item[1] == "1":
				temp[item[0]] = "Male"
			else:
				temp[item[0]] = ""

		elif item[0] == "BaptizedAtCrosspointe":
			if item[1] == "1":
				temp[item[0]] = "Yes"
			else:
				temp[item[0]] = "No"

		elif item[0] == "Status":
			try:
				temp[item[0]] = item[1].split(' ',1)[0]
			except:
				temp[item[0]] = ""

		elif item[0] == "NewResident":
			if item[1] == "1":
				temp[item[0]] = "Yes"
			else:
				temp[item[0]] = "No"

		elif item[0] == "Seeker":
			if item[1] == "1":
				temp[item[0]] = "Yes"
			else:
				temp[item[0]] = "No"

		elif item[0] == "Newsletter":
			if item[1] == "1":
				temp[item[0]] = "Yes"
			else:
				temp[item[0]] = "No"

		elif item[0] == "MarketingResponse":
			if item[1] == "1":
				temp[item[0]] = "Yes"
			else:
				temp[item[0]] = "No"

		elif item[0] == "MailingAddress":
			try:
				Street, Other = item[1].splitlines()
				City, Other = Other.split(', ')
				State, Postcode = Other.split(' ')
			except Exception:
				Street, City, State, Postcode = "","","",""
				pass
			temp["MailingStreet"] = Street
			temp["MailingCity"] = City
			temp["MailingState"] = State
			temp["MailingPostcode"] = Postcode

		else:
			temp[item[0]] = item[1]

	cleanData.append(temp)

cleanData.pop(0)

c.writerow(cleanData[0].keys())
import re
for row in cleanData:
	rowData = []
	for i in row.items():
		if i[1] != None:
			try:
				assign = re.sub(r'[^\x00-\x7f]',r'', i[1]) 
			except:
				continue
		rowData.append(assign)
	c.writerow(rowData)
		

