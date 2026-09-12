class Student:  # student class

    #parameterized constructor
    def __init__(self,name,marks):
        self.name = name
        self.marks=marks


s1 = Student("karan aujla",89) #object creation here s1 is the object , and passing value to be initialized by the __init__ to the object
print(s1.name,s1.marks) #printing name and marks field using the s1 object

s2 = Student("Zfar Bhai",98)
print(s2.name,s2.marks)