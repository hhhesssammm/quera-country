class WorkPlaceIsFull(Exception):

    def __str__(self):
        return "work place is full!"

class Consts:

    BASE_PRICE = {'mine': 150, 'school': 100, 'company': 90}


class WorkPlace:
    instances = []

    def __init__(self, name):
        self.name = name
        self.level = 1
        self.expertise = ""
        self.employees = []
        self.capacity = 1
        self.instances.append(self)

    def get_expertise(self):
        return self.expertise

    def get_price(self):
        return Consts.BASE_PRICE[self.expertise]

    def upgrade(self):
        self.level += 1
        self.calc_capacity()

    def hire(self, person):
        if(len(self.employees) >= self.capacity):
            raise WorkPlaceIsFull

        self.employees.append(person)
        person.work_place = self

    def calc(self):
        return -self.calc_costs()

    def calc_all():
        ret = 0
        for it in WorkPlace.instances:
            ret += it.calc()
        return ret
