class Person(object):
	def __init__(self, person_name, needs_accomodation):
		self.person_name = person_name
		self.needs_accomodation = needs_accomodation
		self.office = None

	def __repr__(self):
		return self.person_name

	def room_type(self):
		return self.__class__.__name__

#creates a Fellow class which inherits from Person
class Fellow(Person):

	person_type = 'Fellow'

	def __init__(self, person_name, needs_accomodation=''):
		super(Fellow,self).__init__(person_name, needs_accomodation)
		self.livingspace = None

	def __repr__(self):
		return self.person_name



class Staff(Person):

	person_type = 'Staff'

	def __init__(self, person_name, needs_accomodation='N'):
		super(Staff, self).__init__(person_name, needs_accomodation)
		self.livingspace = None

	def __repr__(self):
		return self.person_name
