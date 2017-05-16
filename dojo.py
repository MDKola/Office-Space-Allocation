from  models.person import Fellow, Staff
from  models.room import Living_space, Office

class Dojo(object):
        def __init__(self):
                self.all_rooms = []
                self.fellows = []
                self.staff = []
                self.office = []
                self.livingspace = []
                self.all_people = []


        def create_room(self, name, type_of_room):
            room_name = [room.name for room in self.all_rooms]
            if name in room_name:
                 return "Room already exists"

            else:
                if type_of_room == "livingspace":
                        room_type = 'Living_space'
                        new_room = Living_space(room_name, room_type)
                        self.livingspace.append(new_room)
                        self.all_rooms.append(new_room)
                        return "a new livingspace has been created"


                elif type_of_room == 'office':
                        room_type = 'Office'
                        new_room = Office(room_name,room_type)
                        self.office.append(new_room)
                        self.all_rooms.append(new_room)
                        return "new office has been created"


                else:
                        return 'Invalid input'



        def room_occupation(self):
                my_office = self.office
                my_room = self.livingspace
                for office in my_office:
                    if len(office.members) < len(office.capacity):
                        if office not in self.vacant_offices:
                            self.vacant_offices.append(office)
                            self.vacant_rooms.append(office)
                        elif len(office.members) >= len(office.capacity):
                            if office in self.vacant_offices:
                                self.vacant_offices.remove(office)
                                self.vacant_rooms.remove(office)
                for livingspace in my_room:
                    if len(livingspace.members) < len(livingspace.capacity):
                        if livingspace not in self.vacant_livingspace:
                            self.vacant_livingspace.append(livingspace)
                            self.vacant_rooms.append(livingspace)
                        elif len(livingspace.members) >= len(livingspace.capacity):
                            if office in self.vacant_livingspace:
                                self.vacant_livingspace.remove(livingspace)
                                self.vacant_rooms.remove(livingspace)




        def add_person(self, person_name, category, need_accomodation="N"):
                names = [person.name for person in all_people]
                if name in names:
                    return "Name already exists"

                else:
                    if category == 'fellow':
                        new_person = Fellow(name)
                        self.fellows.append(new_person)
                        self.all_people.append(new_person)
