import random

rps_list = ["rock", "paper", "scissors", "xxx"]

for item in range(0,30):
    comp_choise = random.choice(rps_list[:-1])
    print(comp_choise, end="\t")
