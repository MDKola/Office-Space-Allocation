import unittest
from dojo import Dojo


class TestDojo(unittest.TestCase):

	def setUp(self):
		self.dojo = Dojo()

		"""
		checks if the all_rooms list is empty and returns a length
		of
		"""
	def test_create_room_works(self):
		self.assertEqual(len(self.dojo.all_rooms), 0)
		self.dojo.create_room('office1', 'office')
		self.assertEqual(len(self.dojo.all_rooms), 1, 'a new office has been created')

		"""
		checks if a room name exists in the list of all rooms and
		returns an error if the room name exists

		"""
		checks if multiple rooms are created
		"""

	def test_multiple_rooms_created(self):
		self.assertEqual(len(self.dojo.all_rooms), 0)
		self.dojo.create_room('office1', 'office')
		self.dojo.create_room('office2', 'office')
		self.dojo.create_room('office3', 'office')
		self.assertEqual(len(self.dojo.all_rooms), 3)

		"""
		tests if the livingspace room has been created
		"""

	def test_livingspace_created(self):
		self.assertEqual(len(self.dojo.livingspace), 0)
		self.dojo.create_room('mycrib', 'livingspace')
		self.assertEqual(len(self.dojo.livingspace), 1)

		"""
		tests if the office room has been created
		"""

	def test_office_created(self):
		self.assertEqual(len(self.dojo.office), 0)
		self.dojo.create_room('my_office', 'office')
		self.assertEqual(len(self.dojo.office), 1)

	def test_add_person_added(self):
		self.assertEqual(len(self.dojo.fellows), 0)
		self.dojo.add_person('Kola D', 'fellow')
		self.assertEqual(len(self.dojo.fellows),1)


	def test_fellow_is_added(self):
		self.dojo.create_room('office1', 'office')
		self.assertEqual(len(self.dojo.fellows),0)
		self.dojo.add_person('kola', 'fellow')
		self.assertEqual(len(self.dojo.all_rooms), 1, 'Fellow kola has been added to office1 successfully')

	def test_accomodation_is_added(self):
		self.dojo.create_room('my_crib', 'livingspace')
		self.assertEqual(len(self.dojo.fellows), 0)
		self.dojo.add_person('kola', 'fellow', 'Y')
		self.assertEqual(len(self.dojo.all_rooms), 1, 'Fellow kola has been added to my_crib successfully')


	def test_staff_added(self):
		self.dojo.create_room('office1', 'office')
		self.assertEqual(len(self.dojo.staff),0)
		self.dojo.add_person('kola', 'Staff')
		self.assertEqual(len(self.dojo.all_rooms), 1, 'Staff kola has been added to office1 successfully')

	def test_print_room(self):
		self.dojo.create_room('office', 'office1')
		self.dojo.create_room('livingspace', 'living1')
		self.dojo.add_person('kola', 'fellow')
		self.dojo.add_person('deno', 'staff')
		self.assertEqual(self.dojo.print_rooms('office1'), 'rooms printed')
