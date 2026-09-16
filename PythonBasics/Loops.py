
print("------------------------------------------------ while --------------------------------------------------------")

i = 1 #initialization
while i<=5: #condition checking , run loop until it returns false
    print("loop ke andar hunn") #body of the loop statement
    i=i+1 #updating the value of i

print("aab loop ke bahar hun") #loop outside statement

elements = [1,4,9,16,25,36,49,64,81,100]
search = int(input("Enter the number to search : "))
i=0
while i<len(elements):
    if elements[i] == search:
        found = True
        print("Element found at",i,"index")
        break
    i+=1
else:
    print("Element is not present in the list ")

print("------------------------------------------------ for --------------------------------------------------------")
for el in elements:
    print(el,end=" ")

for i in range(1,10):
    pass  #keyword is used to skip a loop / conditional statement