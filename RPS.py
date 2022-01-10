import random

t = ["rock","paper","scissors"]
computer = False

while computer == False:
    player = input("rock or paper or scissors ? ")
    #print(player)
    computer = t[random.randint(0,2)]
    print("computer's choice is {}".format(computer))
    if player == computer:
        print("It is a tie")
    elif player == 'rock':
        if computer == 'paper':
            print("Computer wins")
        else:
            print("Player wins")
    elif player == 'scissors':
        if computer == 'rock':
            print("Computer wins")
        else:
            print("Player wins")
    elif player == 'paper':
        if computer == 'scissors':
            print("Computer wins")
        else:
            print("Player wins")
    computer = False
