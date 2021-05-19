class Person:
    def __init__(self, name, age):
        self.name=name
        self.age=age

    def printAge(self):
        print(f"{self.name} ist {self.age} Jahre Alt")

Tobias = Person("Tobias",14)
Jacek = Person("Jacek",19)
#print(Tobias.name)
#print(Jacek.name)

Tobias.printAge()
Jacek.printAge()
