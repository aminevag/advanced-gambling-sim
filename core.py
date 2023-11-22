import random

try:
   num_dice = int(input("how many faces you need the dice to have: "))
except ValueError:
    num_dice = 6


dice = list(range(1, num_dice))

try:
    balck_listed = int(input("Whats the dark number: "))
    if balck_listed not in dice:
        balck_listed = random.choice(dice)
        print(f"The dark num is {balck_listed}")
except ValueError:
    balck_listed = random.choice(dice)
    print(f"The dark num is {balck_listed}")


try:
    round = int(input("You want to play for(round's): "))
except ValueError:
    round = 2

#////////////////////////////////////////////////////
name_1 = input("p1 name is: ")
if name_1 == "":
    name_1 = "player 1"

s__1 = 0

#////////////////////////////////////////////////////
name_2 = input("p2 name is: ")
if name_2 == "":
    name_2 = "player 2"

s__2 = 0

#////////////////////////////////////////////////////



def core():
    _ = 1
    for x in range(round):
        main()
        _ += 1
        if _ <= round:
            print("*"*9)
            print("*"*9)
            print(f"round {_} start")
            print("*"*9)
            print("*"*9)




def main():
    print("/"*9)
    print(f"{name_1} turn")
    print("/"*9)
    scoren_1 = player(s__1, name_1)
    print(f"{name_1} score is: {scoren_1}")
    print("/"*9)
    print(f"{name_2} turn")
    scoren_2 = player(s__2, name_2)
    print(f"{name_2} score is: {scoren_2}")
    print("/"*9)
    score(scoren_1, scoren_2)



def player(score_1, p1n):
    while True:
        while True:
            gen_1 = random.choice(dice)
            if gen_1 != balck_listed:
                score_1 += gen_1
                print(f"{p1n} you scored: {score_1}")
                choix = input(f"role again {p1n} y/n?: ")
                if choix.lower() == "y":
                    break
                else:
                    return score_1
            else:
                score_1 = 0
                print(f"unlucky your scored {balck_listed}")
                return score_1


def score(score_1, score_2):
    if score_1 > score_2:
        print(f"{name_1} won")
        print(f"{score_1} > {score_2}")
    elif score_1 < score_2:
        print(f"{name_2} won")
        print(f"{score_2} > {score_1}")
    else:
        print("you stupid gambler")
        print(f"{score_1}={score_2}")



core()
