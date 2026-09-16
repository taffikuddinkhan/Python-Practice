class Complex:
    def __init__(self,real,img):
        self.real = real
        self.img = img

    def showcomplex(self):  #this one is called method bcz it is inside the class
        print(self.real,"i +",self.img,"j")

    def add(self,num2):  # it is the older normal add function for the complex numbers
        real_val = self.real + num2.real
        img_val = self.img + num2.img
        return Complex(real_val,img_val)

    def __add__(self,num2):  # it is the older normal add function for the complex numbers
        real_val = self.real + num2.real
        img_val = self.img + num2.img
        return Complex(real_val,img_val)

num1 = Complex(5,7)
num1.showcomplex()
num2 = Complex(2,5)
num2.showcomplex()

print("printed using normal manual method")
num3 = num1.add(num2)  # before using the Dunder function ihave to call the add method then pass the values then store it in to a variable then ican print the value
num3.showcomplex()
print(  )


#Outside class → Function
#Inside class → Method

print("printed using dunder function")
num3 = num1+num2
num3.showcomplex()

# in python __new__() is the constructor which is called by the __init__()


