class Room(object):
	def __init__(self, name, room_type, max_occupants):
		self.name = name
		self.room_type = room_type
		self.max_occupants = max_occupants



class Office(Room):
	def __init__(self, max_occupants=6):


class Living_space(Room):
	def __init__(self,max_occupants=4):
		