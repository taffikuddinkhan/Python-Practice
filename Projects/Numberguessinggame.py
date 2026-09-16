from random import randint

random_num = randint(1,10)
while True:
    value = input("Hi user ! , Guess the number or u can Quit by (Q) : ")
    if value == "Q":
        print("Thank you user !")
        break

    value = int(value)

    if value == random_num:
        print("7 karod bhai , u have choose the right one ")
        break
    if value < random_num:
        print("Your number is small , choose a bigger one")
    else:
        print("Your number is big , choose a smaller one")

print("============================================== GAME OVER ==================================================")