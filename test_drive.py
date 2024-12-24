class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        new_floor = 0
        while new_floor < self.number_of_floors:
            new_floor += 1
            print(new_floor)