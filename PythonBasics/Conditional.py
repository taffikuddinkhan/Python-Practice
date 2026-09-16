light = input("Enter light : ")

if light == "red":
    print("stop")
elif light == "yellow":
    print("Start ur engines")
elif light == "green":
    print("go ..")
else:
    print("light is broken")

#value assign based on condition---------------------------------------------

food = input("Food : ")
eat = "yes" if food == "biryani" else "no"
print(eat)
print("Hydrabadi") if food == "biryani" or food == "zafar bhai biryani" else print("pulao")

age = int(input("Enter age : "))
vote = ("no","yes") [age >= 18]
print(vote)
