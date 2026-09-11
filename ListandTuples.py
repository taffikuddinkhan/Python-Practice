

print("----------------------------------------------- LIST ----------------------------------------------------------")
student1=["TAFFIK",266320100077,78.1]  #List can contain multiple datatypes
print(student1) #list are muteable / means we can change them
marks = [12,34,51.1,45,67.7,89]  #list declaration
print(marks) #list print
print(marks[0],marks[1]) #indexed based access
print(marks[1:4]) #index slicing
print(marks[-3:-1]) #negative index slicing

#                ======================== Methods ================================

marks.append(80.1) #add element in list at the end
print(marks)
marks.sort() #sort in ascending order
print(marks)
marks.sort(reverse=True) #sort in descending order
print(marks)
marks.reverse() #reverse the total list
marks.insert(0,120) #insert at specific position
print(marks)
marks.remove(12) #remove the first occurrence of given element
print(marks)
#and many more methods are available for the list


print(" ---------------------------------------------- TUPLES --------------------------------------------------------")
tup = (10,11,9,2,4,1,11) # The tuple is completely immutable as like String
print(tup)
test = (2) #python will treat this as a integer , so make sure to give a comma if u are declaring single element in tuple
print(type(test)) #the type will be int
print(tup.index(9)) #return the index of the given value
print(tup.count(11)) #return the occurrence of the give element

print("practice questions  ")
#wpa to ask the user to enter their favorite movies name and store them in a list
mov_list=[]
mov1 = input("Enter ur first favorite movie : ")
mov_list.append(mov1)
mov2 = input("Enter ur second favorite movie : ")
mov_list.append(mov2)
mov3 = input("Enter ur third favorite movie : ")
mov_list.append(mov3)
print("Your favorite movie list is : " , mov_list)

# wap to check if a list contains a palindrome of elements
