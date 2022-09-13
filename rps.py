import random
usr = input("enter your choice (rock , paper, scissors): ")
opt = ['rock', 'paper','scissors']
comp = random.choice(opt)
print(f"\n your choice {usr}, computer choice {comp}.\n")
if usr == comp:
    print(f"both selected {usr}, its a tie!")
elif usr == 'rock':
    if comp == 'scissors':
        print("rock smashes scissors, you win")
    else:
        print("paper covers rock, you lose")
elif usr == 'paper':
    if comp == "rock":
        print("paper covers rock, you win")
    else:
        print("scissors cut paper, you loose")
elif usr == 'scissors':
    if comp == 'paper':
        print("scissors cut paper, you win")
    else:
        print("rock breaks scissors, you loose")
