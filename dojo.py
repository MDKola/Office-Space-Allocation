from  models.person import Fellow, Staff
from  models.room import Living_space, Office
import random

class Dojo(object):
    def __init__(self):
        self.all_rooms = []
        self.all_people = []
        self.vacant_rooms = []
        self.vacant_offices = []
        self.vacant_livingspace = []
        self.unallocated = []
        self.fellows = []
        self.staff = []
        self.office = []
        self.livingspace = []
        

    def create_room(self, room_name, type_of_room):
        rooms = [room.room_name for room in self.all_rooms]
        if room_name in rooms:
             print ("Room already exists. Please use a different room name")

        else:
            if type_of_room == "livingspace":
                    room_type = 'Living_space'
                    new_room = Living_space(room_name)
                    self.livingspace.append(new_room)
                    self.all_rooms.append(new_room)
                    print ("a new livingspace, %s has been created" %new_room.room_name)


            elif type_of_room == 'office':
                    room_type = 'Office'
                    new_room = Office(room_name)
                    self.office.append(new_room)
                    self.all_rooms.append(new_room)
                    print ("a new office, %s has been created" %new_room.room_name)


            else:
                    print ('Invalid input')



    def room_occupation(self):
        my_office = self.office
        my_livingspace = self.livingspace
        for office in my_office:
            if len(office.members) < office.max_occupants:
                if office not in self.vacant_offices:
                    self.vacant_offices.append(office)
                    self.vacant_rooms.append(office)
                elif len(office.members) >= office.max_occupants:
                    if office in self.vacant_offices:
                        self.vacant_offices.remove(office)
                        self.vacant_rooms.remove(office)
        
        for livingspace in my_livingspace:
            if len(livingspace.members) < livingspace.max_occupants:
                if livingspace not in self.vacant_livingspace:
                    self.vacant_livingspace.append(livingspace)
                    self.vacant_rooms.append(livingspace)
                elif len(livingspace.members) >= livingspace.max_occupants:
                    if office in self.vacant_livingspace:
                        self.vacant_livingspace.remove(livingspace)
                        self.vacant_rooms.remove(livingspace)




    def add_person(self, person_name, category, needs_accomodation="N"):
                names = [person.person_name for person in self.all_people]
                if person_name in names:
                    print ("Name already exists")

                else:
                    if category == 'fellow':
                        new_person = Fellow(person_name)
                        self.fellows.append(new_person)
                        self.all_people.append(new_person)
                        self.room_occupation()
                        if self.office or self.livingspace:
                            if not self.vacant_offices:
                                self.unallocated.append(new_person)
                                print ('No vacant offices or all available offices are full')

                            else:
                                random_office = random.choice(self.vacant_offices)
                                new_person.office = random_office
                                random_office.members.append(new_person)
                                print ('Fellow %s added successfully to office %s'%(new_person.person_name,random_office.room_name))
                            if needs_accomodation == 'Y':
                                self.room_occupation()
                                if not self.vacant_livingspace:
                                    print ('no vacant livingspace in the dojo')

                                else:
                                    random_livingspace = random.choice(self.vacant_livingspace)
                                    new_person.livingspace = random_livingspace
                                    random_livingspace.members.append(new_person)
                                    print ('Fellow %s added successfully to living space %s'%(new_person.person_name,random_livingspace.room_name))

                    elif category == 'staff':
                        new_person = Staff(person_name)
                        self.staff.append(new_person)
                        self.all_people.append(new_person)
                        if self.office:
                            self.room_occupation()
                            if not self.vacant_offices:
                                self.unallocated.append(new_person)
                                print('No vacant offices available')
                            else:
                                random_office = random.choice(self.vacant_offices)
                                new_person.office= random_office
                                random_office.members.append(new_person)
                                print ('Staff %s has been added to office %s successfully'%(new_person.person_name, random_office.room_name))

                        else:
                            self.unallocated.append(new_person)
                            print ('No vacant office. Please create a room')
