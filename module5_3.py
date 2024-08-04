class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        if 1 <= new_floor <= self.number_of_floors:
            print(*[i for i in range(1,new_floor+1)])
        else:
            print('Такого этажа не существует')
    def __len__(self):
        return self.number_of_floors
    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {len(self)}'
    def __eq__(self,other):
        if isinstance(other,int):
            return self.number_of_floors==other.number_of_floors
    def __lt__(self,other):
        if isinstance(other,int):
            return self.number_of_floors<other.number_of_floors
    def __le__(self,other):
        if isinstance(other,int):
            return self.number_of_floors<=other.number_of_floors
    def __gt__(self,other):
        if isinstance(other,int) or isinstance(other, House):
            return self.number_of_floors>other.number_of_floors
    def __ge__(self,other):
        if isinstance(other,int):
            return self.number_of_floors>=other.number_of_floors
    def __ne__(self,other):
        if isinstance(other,int):
            return self.number_of_floors!=other
    
    def __add__(self,value):
        if isinstance(self,House) and isinstance(value,int):
            self.number_of_floors+=value
            return self.number_of_floors
        else:
            print ('Неверный тип данных')
    def __radd__(self,value):
        return self.__add__(value)
    def __iadd__(self,value):
        return self.__add__(value)

h1=House('Саларьево',15)
h2=House('Urban city',13)
h1.go_to(7)
h1.go_to(16)
h2.go_to(12)
print(h1>h2)
print(str(h1))
print(h1!=15)

