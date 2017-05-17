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
            if len(office.members) < len(office.max_occupants):
                if office not in self.vacant_offices:
                    self.vacant_offices.append(office)
                    self.vacant_rooms.append(office)
                elif len(office.members) >= len(office.max_occupants):
                    if office in self.vacant_offices:
                        self.vacant_offices.remove(office)
                        self.vacant_rooms.remove(office)
        for livingspace in my_room:
            if len(livingspace.members) < len(livingspace.max_occupants):
                if livingspace not in self.vacant_livingspace:
                    self.vacant_livingspace.append(livingspace)
                    self.vacant_rooms.append(livingspace)
                elif len(livingspace.members) >= len(livingspace.max_occupants):
                    if office in self.vacant_livingspace:
                        self.vacant_livingspace.remove(livingspace)
                        self.vacant_rooms.remove(livingspace)




    def add_person(self, person_name, category, needs_accomodation="N"):
                names = [person.name for person in self.all_people]
                if name in names:
                    return "Name already exists"

                else:
                    if category == 'fellow':
                        new_person = Fellow(name)
                        self.fellows.append(new_person)
                        self.all_people.append(new_person)
                        self.room_occupation()
                        if self.office or self.livingspace:
                            if not self.vacant_offices:
                                self.unallocated.append(new_person)
                                print ('No vacant offices')

                            else:
                                random_office = random.choice(self.vacant_offices)
                                new_person.office = random_office
                                randoom_office,members.append(new_person)
                                print ('Fellow %s added successfully to %s'%(new_person.name,random_office.name))
                            if needs_accomodation == 'Y':
                                self.room_occupation()
                                if not self.vacant_livingspace:
                                    print ('no vacant livingspace')

                                else:
                                    random_livingspace = random.choice(self.vacant_livingspace)
                                    new_person.livingspace = random_livingspace
                                    random_livingspace.members.append(new_person)

                    elif category == 'staff':
                        new_person = Staff(name)
                        self.staff.append(new_person)
                        self.all_people.append(new_person)
                        if self.office:
                            self.check_room_is_vacant()
                            if not self.vacant_offices:
                                self.unallocated.append(new_person)
                                print('No vacant offices available')
                            else:
                                random_office = random.choice(self.vacant_offices)
                                new_person.office= random_office
                                random_office.members.append(new_person)
                                print ('Staff %s has been added to office %s successfully'%(new_person.name, random_office.name))

                        else:
                            self.unallocated.append(new_person)
                            print ('No vacant office. Please create a room')
