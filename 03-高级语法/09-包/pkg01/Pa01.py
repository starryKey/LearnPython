

class Student():
    def __init__(self, name="Tom", age=18):
        self.name = name
        self.age = age

    def say(self):
        print("My name is {0}, I am {1} years old".format(self.name, self.age))


def sayHello():
    print("Hello,I am Jack")
