import random
print("                         What is the number?                         ")
print("\n \nyou have to guess number in between 1 to 100.")
guess= random.randint(1,100)
count=0
while True:
    user=int(input("Enter your guess:"))
    if user>guess:
        print("Higher...")
        count+=1
    elif user<guess:
        print("Lower....")
        count+=1
    else:
        print("WoW, You got guess right.\nCONGRATULATION!!!!!")
        print("and you take ",count," tries to guess right number")
        break