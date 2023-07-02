import random

Choice = ["Rock", "Paper", "Scissors"]

while True:
    print("Rock-Paper-Scissors Game:")

    userScore, computerScore = 0, 0

    for i in range(1, 6):
        print("Round ", i, " Start:")

        print("Please select any option")

        print("1. Rock", "2. Paper", "3. Scissors", sep="\n")

        ch = int(input())

        if ch == 1:
            print("You selected Rock")
            ch = "Rock"
        elif ch == 2:
            print("You selected Paper")
            ch = "Paper"
        elif ch == 3:
            print("You selected Scissors")
            ch = "Scissors"
        else:
            print("Invalid Choice")
            break

        cc = random.choice(Choice)
        print("Computer selected ", cc)

        if ch == cc:
            print("This round is Draw", sep="\n")
        elif (
            (ch == "Paper" and cc == "Rock")
            or (ch == "Rock" and cc == "Scissors")
            or (ch == "Scissors" and cc == "Paper")
        ):
            userScore += 1
            print("You Win this round", sep="\n")
        else:
            computerScore += 1
            print("Computer Win this round", sep="\n")

    if userScore > computerScore:
        print("YOU WON !")
        print(
            "Your Score is : ",
            userScore,
            " Computer Score is : ",
            computerScore,
            sep=" ",
        )
    elif userScore < computerScore:
        print("YOU LOST !")
        print(
            "Your Score is : ",
            userScore,
            " Computer Score is : ",
            computerScore,
            sep=" ",
        )
    else:
        print(" DRAW !")
        print(
            "Your Score is : ",
            userScore,
            " Computer Score is : ",
            computerScore,
            sep=" ",
        )

    uc = input("You want to play again (y/n)")
    if uc == "y":
        continue
    else:
        break
