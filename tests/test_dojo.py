import unittest
from dojo import Dojo


class TestDojo(unittest.TestCase):
	
	def setup(self):
		self.dojo = Dojo()

		#check whether the room list is empty and test when a room is added by returning "room added successfully"
	def test_create_room_works(self):
		self.assertEqual(len(self.dojo.all_rooms), 0)
		self.dojo.create_room('office1', 'Office')
		self.assertEqual(len(self.dojo.all_rooms), 1, 'room added successfully')

		#check if the room name entered is present in all rooms list and returns error with message "Room name Already exists"
	def test_duplicate_rooms(self):
		self.dojo.create_room("office1", "Office")
		room_name = [j.name for j in self.dojo.all_rooms]
		self.assertIn("office1", room_name)
		msg = self.dojo.create_room("office1", "office")
		self.assertEqual(msg, "Room name Already exists") 

        """checks if all_rooms list is empty and creates office1,office2,office3 in the office category 
        and checks if the all_roomn list has a number of three items
        """
	def test_multiple_rooms_created(self):
    	self.assertEqual(len(self.dojo.all_rooms), 0)
    	self.dojo.create_room('office1', 'office')
    	self.dojo.create_room('office2', 'office')
    	self.dojo.create_room('office3', 'office')
    	self.assertEqual(len(self.dojo.all_rooms), 3)

    	#checks that when the livingspace room list is empty it returns a list length of 0 and when room called "my_crib" is added, the list length returns 1.
    def test_living_space_is_created(self):
        self.assertEqual(len(self.dojo.livingspace), 0)
        self.dojo.create_room('my_crib', 'livingspace')
        self.assertEqual(len(self.dojo.livingspace), 1)

    def test_add_person_added(self):
       
        #when a person is added, the all_people list length increases approprietly 
        self.assertEqual(len(self.dojo.all_people), 0)
        self.dojo.add_person('kobby', 'Staff')
        self.dojo.add_person('bett', 'Fellow')
        self.assertEqual(len(self.dojo.all_people), 2)
    

     







