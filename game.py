import random
x = int(input("Your assumption between 1-6 is:"))
y = random.randint(1, 6)
print("Lottery number is " + str(y))
if x == y:
    print("You have won. Congrats!!!!!!")
else:
    print("Sorry you've lost but keep going!!!!!!!!")
