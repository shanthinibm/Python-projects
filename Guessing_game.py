import random

name = input("Hello, what is your name?")
print(name)
computer = random.randint(1,10)
print("okay!" +name+" I am Guessing a number between 1 and 10:")
attempts=0
while attempts<5:
    player = int(input())
    print(player)
    attempts = attempts + 1
    if player < computer:
        print("Your guess is too low")
    elif player > computer:
        print("Your guess is higher")
    else:
        print("You guessed the number in {} tries!".format(attempts))
        break
    if attempts == 5:
        print("No: of attempts are over and the number was {}".format(computer))
        break

