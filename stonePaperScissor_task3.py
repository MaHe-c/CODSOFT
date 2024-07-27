import random

print("Stone Paper Scissors Game : ")
print("----------------------------")

print("\nRule 1 : Stone smashes scissors,so stone wins!")
print("Rule 2 : Paper covers stone,so paper wins!")
print("Rule 3 : Scissors cut paper,so scissor wins!")

options = ("stone","paper","scissor")
playing = True
player_mark = 0
computer_mark = 0

while playing:
    player = None
    computer = random.choice(options)

    while player not in options:
        player = input("\nEnter your choice (stone / paper / scissor) : ")

    print(f"\nPlayer : {player}")
    print("\nNow its computer turn")
    print(f"\nComputer : {computer}")



    if player == computer:
        print("\nIts a tie :)")

    elif player == "stone" and computer == "scissor":
        print("\nYou win :) Computer lose ")
        player_mark += 1

    elif player == "paper" and computer == "stone":
        print("\nYou win :) Computer lose ")
        player_mark += 1

    elif player == "scissor" and computer == "paper":
        print("\nYou win :) Computer lose ")
        player_mark += 1

    else:
        print("\nYou lose :( Computer win")
        computer_mark += 1

    play_Again = input("\nPlay Again? (Y/N) : ").lower()
    if not play_Again == "y":
        playing = False

print("\nThanks for playing :)")
print(f"\nPlayer Mark : {player_mark}")
print(f"\nComputer Mark : {computer_mark}")