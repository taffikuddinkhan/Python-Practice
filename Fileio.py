import os

file = open("demo.txt","r") # to open a file and pass r argument to read the file
data = file.read() #reading the file by storing it into data variable
print(data)
f=open("demo.txt","w")
f.write("i want to learn javascript") # delete all the existing text from file and add the new ones
print(type(data))
print(type(file))

with open("demo.txt","r") as f:  #when we use the with keyword we don't need to close the file , it will automatically close
    k = f.read()
    print(k)
file.close()

os.remove("sample.txt")