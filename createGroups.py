def checker(key, value):
	if value is not None:
			data[key] = value
	else: 
		data[key] = ""

import json, requests, MySQLdb,urllib
from config import mysqlConfig, elvantoConfig

data = {
	'name':'',
	'status':'',
	'meeting_address':'',
	'meeting_city':'',
	'meeting_postcode':'',
	'meeting_country':'',
	'meeting_start_date':'',
	'meeting_start_time':'',
	'meeting_end_date':'',
	# 'meeting_frequency':
	# 	{
	# 		'type':'',
	# 		'count':'',
	# 		'day':'',
	# 		'occurrence':'',
	# 	},
	# 'fields':
	# 	{
	# 		'categories':'',
	# 		'departments':'',
	# 		'demographics':'',
	# 		'locations':'',
	# 	},
}


# MySQL Select
db = MySQLdb.connect(mysqlConfig.host, mysqlConfig.user, mysqlConfig.password, mysqlConfig.database)
cursor = db.cursor()
stmt = ''' SELECT Name, Day, Time, Directions
		FROM tblMinistries 
		WHERE Status != '4';
		'''
cursor.execute(stmt)
headers = {'content-type': 'application/json'}

url = elvantoConfig.baseUrl+'groups/create.json'

results = cursor.fetchone()
i=0
while results is not None:
	checker('name', results[0])
	checker('meeting_address', results[3])
	checker('meeting_address', results[3])
	# checker('meeting_frequency[\'day]', results[1])
	checker('meeting_start_time', results[2])

	r = requests.post(url, auth=(elvantoConfig.apiKey,'x'), headers=headers, data=json.dumps(data))
	results = cursor.fetchone()



db.close()


# 