class Dojo(object):
        def __init__(self):
                self.all_rooms = []
                self.fellows = []
                self.staff = []
                self.office = []
                self.livingspace = []
                self.all_people = []
        

        def create_room(self, room_name, type_of_room):
                if type_of_room == "livingspace":
                        room_type = 'Livingspace'
                        new_room = Livingspace(room_name)
                        self.livingspace.append(new_room)
                        self.all_rooms.append(new_room)
                        print ("A new Livingspace, %s created successfully" % (new_room))

                elif type_of_room == 'office':
                        room_type = 'Office'
                        new_room = Office(room_name)
                        self.office,append(new_room)
                        self.all_rooms.append(new_room)
                        print ("A new office, %s created successfully" % (new_room)

                else:
                        return 'Invalid input'



        

        def add_person(self, person_name, category, need_accomodation="N"):
                pass

        def room_occupation(self):
                pass

       