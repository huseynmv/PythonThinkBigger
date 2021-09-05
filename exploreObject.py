class Person:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age
    def abc():
        print("salam")
    def cde():
        print("sagol")


def exploreObject(obj):
    for property, value in vars(obj).items():
        print(property, ":", value)
    method_list = [method for method in dir(Person) if method.startswith('__') is False]
    print (method_list)

personn = Person("Huseyn", "Mammadov", 21)
exploreObject(personn)