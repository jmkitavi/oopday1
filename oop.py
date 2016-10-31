class User(object):
	access_level=1
	name=''
	def __init__ (self, name):
		self.name =  name
	def can_access(self, level):
		return self.access_level >= level

class Employee(User):
	access_level = 2
	def can_access(self, level):
		return self.access_level >= level or level == 3

class Manager(Employee):
	access_level =3
	def can_access(self, level):
		return (self.access_level >= level or level in [2,6])


gian = User("Gian")
adrin = Employee("Adrin")
ian = Manager("Limo")
users = [gian,adrin,ian]

for level in range(1,7):
	for u in users:
		print u.name + " can access. level " + str(level) + ' ' + str(u.can_access(level))
	print "\n"