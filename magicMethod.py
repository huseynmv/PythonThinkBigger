class Person:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age
    def abc():
        print("salam")
    def cde():
        print("sagol")

person = Person("Huseyn", "Mammadov", 21)

def Foo(param):
    arr = []
    for index in range(len(param)):
        if index % 2 == 1:
            arr.append(param[index].upper())
        else:
            arr.append(param[index].lower())
    return ''.join(arr)


def magicMethod(param):
    if type (param) is list:
        for i in param:
            print(i, end = ' ')
    elif type(param)==int:
        print(param*param)
    elif type(param)==str:
        print(Foo(param))
    elif isinstance(param, object):
        for property, value in vars(param).items():
            print(property, ":", value)

magicMethod('Helloworld')
magicMethod([1,2,3,4,5])
magicMethod(13)
magicMethod(person)