class Room(object):
	def __init__(self, room_name, max_occupants):
		self.room_name = room_name
		self.max_occupants = max_occupants
		self.members= []

	def __repr__(self):
		return self.room_name

	def add_person(self,person):
		self.max_occupants-=1
		return self.max_occupants
	@property
	def room_type(self):
		return room.__class__.__name__


class Office(Room):
	def __init__(self, room_name, max_occupants=6):
		super(Office, self).__init__(room_name,max_occupants=6)

	def __repr__(self):
		return self.room_name


class Living_space(Room):
	def __init__(self,room_name,max_occupants=4):
		super(Living_space, self).__init__(room_name,max_occupants=4)

	def __repr__(self):
		return self.room_name
