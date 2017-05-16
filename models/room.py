class Room(object):
	def __init__(self, name, room_type, max_occupants):
		self.name = name
		self.room_type = room_type
		self.max_occupants = []

	def __repr__(self):
		return self.name

	def add_person(self,person):
		self.capacity = self.capacity -1
		return self.capacity

	def room_type(self):
		return room.__class__.__name__


class Office(Room):
	def __init__(self, name, room_type,max_occupants=6):
		super(Office, self).__init__(name, room_type,max_occupants=6)

	def __repr__(self):
		return self.name


class Living_space(Room):
	def __init__(self,name,room_type,max_occupants=4):
		super(Living_space, self).__init__(name, room_type,max_occupants=4)

	def __repr__(self):
		return self.name
