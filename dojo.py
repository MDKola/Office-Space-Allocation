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
        #checks roomtype, creates the room and appends to appropriate room list
        print(' ')
        print (('--')*50)

        rooms = [room.room_name for room in self.all_rooms]
        if room_name in rooms:
             print("Room already exists. Please use a different room name")
             print(' ')


        else:
            if type_of_room == "livingspace":
                    room_type = 'Living_space'
                    new_room = Living_space(room_name)
                    self.livingspace.append(new_room)
                    self.all_rooms.append(new_room)
                    print("A new livingspace called %s has been created"\
                     % str(new_room.room_name))
                    print(' ')




            elif type_of_room == 'office':
                    room_type = 'Office'
                    new_room = Office(room_name)
                    self.office.append(new_room)
                    self.all_rooms.append(new_room)
                    print ("a new office, {} has been created" .format(new_room.room_name))
                    print(' ')



            else:
                    print ('Invalid input')
                    print(' ')




    def room_occupation(self):
        #checks room vacancy
        my_office = self.office
        my_livingspace = self.livingspace
        for office in my_office:
            # add office to vacant list if not in vacant list
            if len(office.members) < office.max_occupants:
                if office not in self.vacant_offices:
                    self.vacant_offices.append(office)
                    self.vacant_rooms.append(office)
                    #remove full office from vacant rooms list
                elif len(office.members) >= office.max_occupants:
                    if office in self.vacant_offices:
                        self.vacant_offices.remove(office)
                        self.vacant_rooms.remove(office)

        for livingspace in my_livingspace:
            #add office to vacant list of livingspaces
            if len(livingspace.members) < livingspace.max_occupants:
                if livingspace not in self.vacant_livingspace:
                    self.vacant_livingspace.append(livingspace)
                    self.vacant_rooms.append(livingspace)
                    #remove office full office from vacant list of rooms
                elif len(livingspace.members) >= livingspace.max_occupants:
                    if office in self.vacant_livingspace:
                        self.vacant_livingspace.remove(livingspace)
                        self.vacant_rooms.remove(livingspace)




    def add_person(self, person_name, category, needs_accomodation="N"):
                #adds new person to rooms
                names = [person.person_name for person in self.all_people]
                if person_name in names:
                    print ("Name already exists")
                    print(' ')


                else:
                    if category == 'fellow':
                        new_person = Fellow(person_name)
                        self.fellows.append(new_person)
                        self.all_people.append(new_person)
                        self.room_occupation()
                        #add person to vacant rooms available
                        if self.office or self.livingspace:
                            if not self.vacant_offices:
                                self.unallocated.append(new_person)
                                print ('No vacant offices or all available offices are full')
                                print(' ')


                            else:
                                random_office = random.choice(self.vacant_offices)
                                new_person.office = random_office
                                if len(random_office.members) < random_office.max_occupants:
                                    random_office.members.append(new_person)
                                    print ('Fellow {0} added successfully to office {1}'.format(new_person.person_name,str(random_office.room_name)))
                                    print(' ')

                                else:
                                    print ("this room is full")
                                    print(' ')


                            if needs_accomodation == 'Y':
                                self.room_occupation()
                                if not self.vacant_livingspace:
                                    print ('no vacant livingspace in the dojo')

                                else:
                                    random_livingspace = random.choice(self.vacant_livingspace)
                                    new_person.livingspace = random_livingspace
                                    if len(random_livingspace.members) < random_livingspace.max_occupants:
                                        random_livingspace.members.append(new_person)
                                        print ('Fellow {} added successfully to living space {}'.format(new_person.person_name,random_livingspace.room_name))
                                        print(' ')

                                    else:
                                        print('This room is full')
                                        print(' ')



                    elif category == 'staff':
                        new_person = Staff(person_name)
                        self.staff.append(new_person)
                        self.all_people.append(new_person)
                        if self.office:
                            self.room_occupation()
                            if not self.vacant_offices:
                                self.unallocated.append(new_person)
                                print('No vacant offices available')
                                print(' ')

                            else:
                                random_office = random.choice(self.vacant_offices)
                                new_person.office= random_office
                                if len(random_office.members) < random_office.max_occupants:
                                    random_office.members.append(new_person)
                                    print ('Staff {} has been added to office {} successfully'.format(new_person.person_name, random_office.room_name))
                                    print(' ')

                                else:
                                    print ("this room is full")
                                    print(' ')



                        else:
                            self.unallocated.append(new_person)
                            print ('No vacant office. Please create a room')
                            print(' ')


    def print_room(self):
         pass
