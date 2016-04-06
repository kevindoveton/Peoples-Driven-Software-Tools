# Elvanto Config
class elvantoConfig(object):
	"""docstring for ClassName"""
	baseUrl = 'https://api.elvanto.com/v1/'
	dataFormat = 'json' # valid options are php, json or xml
	apiKey = '###################' # Your api key from elvanto

class urls(elvantoConfig):
	class people(object):
		baseUrl = elvantoConfig.baseUrl + 'people/'
		getAll = baseUrl + 'getAll.' + elvantoConfig.dataFormat
		search = baseUrl + 'search.' + elvantoConfig.dataFormat
		getInfo = baseUrl + 'getInfo.' + elvantoConfig.dataFormat
		create = baseUrl + 'create.' + elvantoConfig.dataFormat
		edit = baseUrl + 'edit.' + elvantoConfig.dataFormat
		remove = baseUrl + 'remove.' + elvantoConfig.dataFormat
		currentUser = baseUrl + 'currentUser.' + elvantoConfig.dataFormat
		class categories(object):
			baseUrl = elvantoConfig.baseUrl + 'people/categories/'
			getAll = baseUrl + 'getAll.' + elvantoConfig.dataFormat
		class customFields(object):
			baseUrl = elvantoConfig.baseUrl + 'people/customFields/'
			getAll = baseUrl + 'getAll.' + elvantoConfig.dataFormat

	class groups(object):
		baseUrl = elvantoConfig.baseUrl + 'groups/'
		getAll = baseUrl + 'getAll.' + elvantoConfig.dataFormat
		getInfo = baseUrl + 'getInfo.' + elvantoConfig.dataFormat
		create = baseUrl + 'create.' + elvantoConfig.dataFormat
		edit = baseUrl + 'edit.' + elvantoConfig.dataFormat
		remove = baseUrl + 'remove.' + elvantoConfig.dataFormat
		addPerson = baseUrl + 'addPerson.' + elvantoConfig.dataFormat
		removePerson = baseUrl + 'removePerson.' + elvantoConfig.dataFormat
# MySQL Config
class mysqlConfig:
	host = 'localhost' # host of the mysql db containing data
	user = 'user' # Username of mysql user
	password = 'password' # password of mysql user
	database = 'pds' # mysql database containing pds data


