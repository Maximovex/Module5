class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        if 1 <= new_floor <= self.number_of_floors:
            print(*[i for i in range(1,new_floor+1)])
        else:
            print('Такого этажа не существует')

h1=House('Саларьево',15)
h1.go_to(7)
h1.go_to(16)

