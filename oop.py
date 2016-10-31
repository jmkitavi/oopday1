class User(object):
	access_level=1
	name=''
	def __init__ (self,name):
		self.name =  name
	def can_access(level):
		return access_level > level

class Employee(User):
	def can_access(level):
		return (access_level> level or level =3)

class Manager(Employee):

	def can_access(level):
		return (access_level> level or (level in [2,3]))
