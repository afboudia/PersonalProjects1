import random

choices = ["rock", "paper", "scissors"]
tie = "tie game  we go agaiyn"
playerwin = "player wins"
botwin = "bot wins"

while (True):
    player = input("Enter your choice (rock, paper, scissors): ").lower()
    if player not in choices:
        print("stick with the program")
    
    else:
        num = random.randint(0, 2)
        bot = choices[num]
        print(bot)
        if player == "rock":
            if bot == "scissors":
                print(playerwin)
                break
            elif bot == "paper":
                print(botwin)
                break
            else:
                print(tie)
        elif player == "scissors":
            if bot == "rock":
                print(botwin)
                break
            elif bot == "paper":
                print(playerwin)
                break
            else:
                print(tie)
        else:
            if bot == "rock":
                print(playerwin)
                break
            elif bot == "scissors":
                print(botwin)
                break
            else:
                print(tie)

    