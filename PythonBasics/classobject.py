class Student:  # student class

    #parameterized constructor
    def __init__(self,name,marks):
        self.name = name
        self.marks=marks


class Person:
    __name = "taffik"

    def __hello(self):  # private method inside the class . the private fields have sign " __ " before the method or attribute name
        print("hello bhai ! ")

    def welcome(self):
        self.__hello()


s1 = Student("karan aujla",89) #object creation here s1 is the object , and passing value to be initialized by the __init__ to the object
print(s1.name,s1.marks) #printing name and marks field using the s1 object

s2 = Student("Zfar Bhai",98) #we can create multiple student type objects
print(s2.name,s2.marks)
#
# del s2.name  #we can delete attribute by using the del keyword
# print(s2.name) #error - student object has no attribute "name"

p1 = Person() #person class object creation
p1.welcome() #it will call the welcome method , then welcome will call the hello method
p1.__hello()  #it will give error because the method hello is private

