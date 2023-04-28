# Name : Umm e Zainab 
# Roll No : F22BSEEN1E02063
class Facility:
    def _init_(self, name, location):
        self.name = name
        self.location = location

class Campus(Facility):
    def _init_(self, name, location, num_buildings, num_students):
        super()._init_(name, location)
        self.num_buildings = num_buildings
        self.num_students = num_students
        self.buildings = []

    def add_building(self, building):
        self.buildings.append(building)

    def remove_building(self, building):
        self.buildings.remove(building)

    def get_buildings(self):
        return self.buildings

class Building(Facility):
    def _init_(self, name, location, num_floors, num_classrooms, num_labs):
        super()._init_(name, location)
        self.num_floors = num_floors
        self.num_classrooms = num_classrooms
        self.num_labs = num_labs
        self.classrooms = []
        self.labs = []

    def add_classroom(self, classroom):
        self.classrooms.append(classroom)

    def remove_classroom(self, classroom):
        self.classrooms.remove(classroom)

    def add_lab(self, lab):
        self.labs.append(lab)

    def remove_lab(self, lab):
        self.labs.remove(lab)

    def get_classrooms(self):
        return self.classrooms

    def get_labs(self):
        return self.labs

class Classroom(Facility):
    def _init_(self, name, location, capacity, equipment):
        super()._init_(name, location)
        self.capacity = capacity
        self.equipment = equipment
        self.course = None

    def assign_course(self, course):
        self.course = course

    def unassign_course(self):
        self.course = None

    def get_course(self):
        return self.course

class Laboratory(Facility):
    def _init_(self, name, location, capacity, equipment):
        super()._init_(name, location)
        self.capacity = capacity
        self.equipment = equipment

class Library(Facility):
    def _init_(self, name, location, num_books):
        super()._init_(name, location)
        self.num_books = num_books