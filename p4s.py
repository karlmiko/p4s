'''

Parking4Students.com management system

created by Karl Michel Koerich
July 10, 2018 

'''

"""Filezilla login: parkflow.space
				user: user
				password: password
				port:
"""

############################################################################################

import pymysql

db = pymysql.connect("www.parkflow.space", "main", "password", "test") #Opens database connection
cursor = db.cursor() #Prepares a cursor object using cursor() method

############################################################################################

def create(table, columns, values):

	sql = """INSERT INTO {} ({}) VALUES ({});""".format(table, ", ".join(columns), ", ".join(values))

	try:
		cursor.execute(sql) #Execute the SQL command
		db.commit() #Commit your changes in the database
	except:
		print("Error")
		db.rollback() #Rollback in case there is any error

def read(table, column, value):

	sql = """SELECT * FROM {} WHERE {} = '{}';""".format(table, column, value)

	cursor.execute(sql) #Execute the SQL command
	result = cursor.fetchall() #Take all the results and add to list result
	return result

def update(table, columns, values):

	empty = ""
	for c, v in columns, values:
		empty += "{} = '{}', ".format(c, v)

	sql = """UPDATE {} SET {} WHERE CustomerID = 1; """

############################################################################################

def mainMenu():

	option = '0'

	while option not in ['1', '2', '3', '4']:
		option = input("\n1 - Create Owner or Driver,\n2 - Search Owner or Driver,\n3 - Update Person,\n4 - Quit.\nType your option and press enter: ")

	if option == '1':
		mainMenuOption1()
	elif option == '2':
		mainMenuOption2()
	elif option == '3':
		mainMenuOption3()
	else:
		return "break"

def mainMenuOption1(): #Creates Owner or Driver

	typePerson = '0'
	columns_owner = ["firstName_Owner", "lastName_Owner", "school_Owner", "email_Owner", "totalSpots_Owner", "totalSpotsAvailable_Owner", "status_Owner", "address_Owner", "comment_Owner"]
	columns_driver = ["firstName_Driver", "lastName_Driver", "school_Driver", "email_Driver", "cellphone_Driver", "area_Driver", "fieldStudy_Driver", "status_Driver", "carModel_Driver", "carColor_Driver"]

	while typePerson not in ['1', '2', '3']: #Types possible: 1 - Owner, 2 - Driver, 3 - Return
		typePerson = input ("\n1 - Create Owner,\n2 - Create Driver,\n3 - Return.\nType your option and press enter: ")

	if typePerson == '1':
		table = "tbOwner"
		columns = columns_owner
	elif typePerson == '2':
		table = "tbDriver"
		columns = columns_driver
	else:
		return

	def iterateColumns(columns):
		values = []
		for column in columns:
			value = input(column + ": ")
			try:
				value = int(value) #See if it is INT and converts back to STR if it is.
				value = str(value)
			except:
				value = "\"" + value + "\""
			values += [value]
		return values

	create(table, columns, iterateColumns(columns))

def mainMenuOption2(): #Search for Owner or Driver

	typePerson = '0'
	typeRetrieve = '0'

	while typePerson not in ['1', '2', '3']: #Types possible: 1 - Owner, 2 - Driver, 3 - Return
		typePerson = input ("\n1 - Search Owner,\n2 - Search Driver,\n3 - Return.\nType your option and press enter: ")

	if typePerson == '1':
		table = "tbOwner"
	elif typePerson == '2':
		table = "tbDriver"
	else:
		return

	while typeRetrieve not in ['1', '2', '3', '4']: # Types possible: 1 - firstName, 2 - school, 3 - email
		typeRetrieve = input ("\nSearch by:\n1 - First name,\n2 - School,\n3 - Email,\n4 - Return.\nType your option and press enter: ")

	if typeRetrieve == '1':
		firstName = input ("First name: ")
		listPersonFound = read(table, "firstName_"+table[2:], firstName)
	elif typeRetrieve == '2':
		school = input ("School: ")
		listPersonFound = read(table, "school_"+table[2:], school)
	elif typeRetrieve == '3':
		email = input ("Email: ")
		listPersonFound = read(table, "email_"+table[2:], email)
	else:
		return

	n = 1
	for person in listPersonFound:
		print ("#"+str(n), person)
		n += 1

	return listPersonFound #The list returned is only used when retrieving for an update.

def mainMenuOption3(): #Search for user

	chosenPersonIndex = 0
	listPersonFound = mainMenuOption2()
	if listPersonFound == []:
		print("\nUser not found!\n")
		return 
	while chosenPersonIndex not in list(range(1, len(listPersonFound)+1)): # +1 in case len(list) is 1
		chosenPersonIndex = input ("Choose a person by its number: ")
		try:
			chosenPersonIndex = int(chosenPersonIndex)
		except Exception:
			pass

	personToUpdate = listPersonFound[chosenPersonIndex-1]

	i = 0 
	for subList in listPerson:
		j = 0
		for person in subList:
			if person == personToUpdate:
				break
			else:
				j += 1
		if person == personToUpdate:
			break
		i += 1

	listPerson[i][j].firstName = input ("First name: ")
	listPerson[i][j].school = input ("School: ")
	listPerson[i][j].email = input ("Email: ")
	listPerson[i][j].homeAddress = input ("Home Address: ")
	print("Person Updated!")

############################################################################################

while True:
	toBreak = mainMenu()
	if toBreak == "break":
		break

db.close()

class Person (object):
	def __init__ (self, firstName, school, email, homeAddress):
		self.firstName = firstName
		self.school = school
		self.email = email
		self.homeAddress = homeAddress
	def __str__ (self):
		return "\t{}\n\t{}\n\t{}\n\t{}\n".format(self.firstName, self.email, self.school, self.homeAddress)


class Owner (Person):
	def __init__ (self, firstName, school, email, homeAddress):
		self.currentlyAvailable = True # 0-false = notAvailable, 1-true = available
		self.listRents = [] # list of rents for the owner
		super().__init__(firstName, school, email, homeAddress)
	def __str__ (self):
		return "Owner\n" + super().__str__() + "\tCurrently available: {}\n\tList of rents: {}".format(self.currentlyAvailable, self.listRents)


class Driver (Person):
	def __init__ (self, firstName, school, email, homeAddress):
		self.currentlyMatched = False # 0-false = noDriveway, 1-true = withDriveway
		self.listRents = [] # list of rents for the driver
		self.listCarpools = [] # list of carpools for the driver
		super().__init__(firstName, school, email, homeAddress)
	def __str__ (self):
		return "Driver\n" + super().__str__() + "\tCurrently matched: {}\n\tList of rents: {}\n\tList of carpools: {}".format(self.currentlyMatched, self.listRents, self.listCarpools)


class Rider (Person):
	def __init__ (self, firstName, school, email, homeAddress):
		self.currentlyMatched = False  # 0-false = noDriveway, 1-true = withDriveway
		self.listCarpools = [] # list of carpools for the driver
		super().__init__(firstName, school, email, homeAddress)
	def __str__ (self):
		return "Rider\n" + super().__str__() + "\tCurrently matched: {}\n\tList of carpools: {}".format(self.currentlyMatched, self.listCarpools)


class Rent (object):
	def __init__ (owner, driver, dateFrom, dateTo):
		self.owner = owner
		self.driver = driver
		self.dateFrom = dateFrom
		self.dateTo = dateTo
