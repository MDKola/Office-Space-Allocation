class Person(object):
	def __init__(self, name, needs_accomodation):
		self.name = name
		self.needs_accomodation = needs_accomodation
		self.office = None

	def __repr__(self):
		return self.name

#creates a Fellow class which inherits from Person
class Fellow(Person):
	def __init__(self, name, needs_accomodation):
		super(Fellow,self).__init__(name)

	def __repr__(self):
		return self.name



class Staff(Person):
	def __init__(self):
		super(Staff, self).__init__(name)

	def __repr__(self):
		return self.name
