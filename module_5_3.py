class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        self.new_floor = new_floor
        if new_floor > self.number_of_floors or new_floor < 1:
            print(f'{new_floor}? Такого этажа не существует!')
        else:
            print(*range(1, new_floor + 1), sep='\n')

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f'Название: ЖК {self.name}, кол-во этажей: {self.number_of_floors}'

    def __eq__(self, other):
        if self.number_of_floors == other.number_of_floors:
            return True
        else:
            return False

    def __lt__(self, other):
        if self.number_of_floors < other.number_of_floors:
            return True
        else:
            return False

    def __gt__(self, other):
        if self.number_of_floors > other.number_of_floors:
            return True
        else:
            return False

    def __ge__(self, other):
        if self.number_of_floors >= other.number_of_floors:
            return True
        else:
            return False

    def __ne__(self, other):
        if self.number_of_floors != other.number_of_floors:
            return True
        else:
            return False

    def __add__(self, value):
        self.number_of_floors += value
        return self

    def __radd__(self, value):
        return self.__add__(value)

    def __iadd__(self, value):
        return self.__add__(value)


h1 = House('Космос', 20)
h2 = House('Great Marble', 10)
print(h1)
print(h2)
print(h2 == h1)
print(h2 < h1)
print(h2 > h1)
print(h2 >= h1)
print(h1 != h2)

h1 = h1 + 15
print(h1)

h2 = 33 + h2
print(h2)

h1 += 11
print(h1)
